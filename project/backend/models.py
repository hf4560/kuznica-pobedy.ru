from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

# Определяем базовый класс для работы с таблицами
Base = declarative_base()

class MediaFileDB(Base):
    __tablename__ = "media_files"
    __table_args__ = {"schema": "media_files"}  # Указываем схему

    id = Column(Integer, primary_key=True, index=True)
    file_uuid = Column(String, unique=True, nullable=False)  # Уникальный идентификатор файла
    original_name = Column(String, nullable=False)           # Оригинальное имя файла
    file_path = Column(String, nullable=False)               # Путь к файлу на сервере
    uploaded_at = Column(DateTime, server_default="CURRENT_TIMESTAMP")  # Время загрузки