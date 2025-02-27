from fastapi import FastAPI, File, UploadFile, Depends, HTTPException
from sqlalchemy.orm import Session
import os
import uuid
from datetime import datetime

app = FastAPI()

# Директория для хранения медиафайлов
MEDIA_DIR = "../../media"
os.makedirs(MEDIA_DIR, exist_ok=True)


@app.post("/upload/")
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
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