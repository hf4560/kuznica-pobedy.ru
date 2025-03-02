from fastapi import FastAPI, File, UploadFile, Depends, HTTPException, Request
from fastapi.responses import FileResponse
import os
import uuid
from database import DataBase  # Импортируем ваш класс DataBase
from models import MediaFileDB, StaticContent, HeaderLink  # Импортируем модель MediaFileDB
from iniparser import Config
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Dict
from redis_client import redis_client
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # или укажите конкретные домены, например ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

# Pydantic модель для валидации
class ContentData(BaseModel):
    content: Dict

class LinkResponse(BaseModel):
    link_to: str
    class_name: str
    text: str


@app.get("/cache/{key}")
async def get_cache(key: str):
    # Попытка получить данные из Redis
    cached_data = redis_client.get(key)
    if cached_data:
        return {"key": key, "value": cached_data}
    else:
        raise HTTPException(status_code=404, detail="Cache not found")

@app.post("/cache/{key}")
async def set_cache(key: str, value: str):
    # Сохраняем данные в Redis с временем жизни 60 секунд
    redis_client.setex(key, 60, value)
    return {"key": key, "value": value}

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


# Получение статического контента
@app.get("/api/static/{component_type}", response_model=Dict)
async def get_static_content(
        component_type: str,
        db=Depends(get_db)
):
    component = db.query(StaticContent).filter(
        StaticContent.component_type == component_type
    ).first()
    if not component:
        raise HTTPException(status_code=404, detail="Component not found")
    return component.content


# Обновление статического контента (только для админов)
@app.put("/api/static/{component_type}", status_code=204)
async def update_static_content(
        component_type: str,
        data: ContentData,
        db=Depends(get_db),
        # Добавьте проверку прав админа
        # user=Depends(get_admin)
):
    component = db.query(StaticContent).filter(
        StaticContent.component_type == component_type
    ).first()

    if component:
        component.content = data.content
    else:
        component = StaticContent(
            component_type=component_type,
            content=data.content
        )
        db.add(component)

    db.commit()


@app.get("/api/headerlinks", response_model=list[LinkResponse])
async def get_links(db=Depends(get_db)):
    links = db.query(HeaderLink).all()
    return links

@app.post("/api/headerlinks")
async def create_link(link: LinkResponse, db=Depends(get_db)):
    db_link = HeaderLink(
        link_to=link.link_to,
        class_name=link.class_name,
        text=link.text
    )
    db.add(db_link)
    db.commit()
    db.refresh(db_link)
    return db_link


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=config.getValue('mediaapi', 'host'), port=int(config.getValue('mediaapi', 'port')))