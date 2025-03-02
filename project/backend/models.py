from sqlalchemy import Column, Integer, String, DateTime, text, JSON, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

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

class StaticContent(Base):
    __tablename__ = 'components'
    __table_args__ = {'schema': 'static_content'}  # Указываем схему

    id = Column(Integer, primary_key=True)
    component_type = Column(String(50), unique=True, nullable=False)
    content = Column(JSON, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

class HeaderLink(Base):
    __tablename__ = 'header_links'
    __table_args__ = {'schema': 'static_content'}  # Указываем схему

    id = Column(Integer, primary_key=True, index=True)
    link_to = Column(String, nullable=False)
    class_name = Column(String, nullable=False)
    text = Column(String, nullable=False)
