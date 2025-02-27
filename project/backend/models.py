from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

class MediaFileDB:
    __tablename__ = "media_files"

    id = Column(Integer, primary_key=True, index=True)
    file_uuid = Column(String, unique=True, nullable=False)  # Уникальный идентификатор файла
    original_name = Column(String, nullable=False)           # Оригинальное имя файла
    file_path = Column(String, nullable=False)               # Путь к файлу на сервере
    uploaded_at = Column(DateTime, default=datetime.utcnow)  # Время загрузки