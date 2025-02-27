from sqlalchemy import Column, Integer, String, DateTime, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class MediaFileDB(Base):
    __tablename__ = "media_files"
    __table_args__ = {"schema": "media_files"}  # Указываем схему

    id = Column(Integer, primary_key=True, index=True)
    file_uuid = Column(String(36), unique=True, nullable=False)
    original_name = Column(String(255), nullable=False)
    file_path = Column(String(512), nullable=False)
    uploaded_at = Column(
        DateTime(timezone=True),  # Добавляем временную зону
        server_default=text("NOW()")  # Используем NOW() для PostgreSQL
    )