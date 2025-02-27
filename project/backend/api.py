from fastapi import FastAPI, File, UploadFile, Depends, HTTPException, Request
from fastapi.responses import FileResponse
import os
import uuid
from database import DataBase  # Импортируем ваш класс DataBase
from models import MediaFileDB  # Импортируем модель MediaFileDB
from iniparser import Config
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

config = Config('config.ini')

# Инициализация базы данных
db_instance = DataBase()
db_instance.connect()
db_instance.create_tables()


# Dependency для получения сессии
def get_db():
    db = db_instance.get_session()
    try:
        yield db
    finally:
        db.close()


# Директория для хранения медиафайлов
MEDIA_DIR = config.getValue('fileserver', 'media')
os.makedirs(MEDIA_DIR, exist_ok=True)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def upload_form(request: Request):
    return templates.TemplateResponse("upload_form.html", {"request": request})

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...), db=Depends(get_db)):
    # Генерируем UUID
    file_uuid = str(uuid.uuid4())

    # Определяем путь для сохранения файла
    file_extension = os.path.splitext(file.filename)[1]
    unique_filename = f"{file_uuid}{file_extension}"
    file_path = os.path.join(MEDIA_DIR, unique_filename)

    # Сохраняем файл
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Сохраняем информацию о файле в БД
    db_file = MediaFileDB(
        file_uuid=file_uuid,
        original_name=file.filename,
        file_path=file_path
    )
    db.add(db_file)
    db.commit()
    db.refresh(db_file)

    # Возвращаем UUID файла
    return {"file_uuid": file_uuid}


@app.get("/media/{file_uuid}")
async def get_file(file_uuid: str, db=Depends(get_db)):
    # Находим файл в базе данных
    db_file = db.query(MediaFileDB).filter(MediaFileDB.file_uuid == file_uuid).first()
    if not db_file:
        raise HTTPException(status_code=404, detail="File not found")

    # Отдаем файл
    return FileResponse(db_file.file_path)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=config.getValue('mediaapi', 'host'), port=int(config.getValue('mediaapi', 'port')))