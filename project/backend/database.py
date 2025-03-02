from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from urllib.parse import quote_plus
from project.backend.iniparser import Config

try:
    config = Config('project/backend/config.ini')
    DATABASE_URL = (f"{config.getValue('database', 'protocol')}://"
                   f"{config.getValue('database', 'user')}:"
                   f"{quote_plus(config.getValue('database', 'password'))}@"
                   f"{config.getValue('database', 'host')}:"
                   f"{config.getValue('database', 'port')}/" 
                   f"{config.getValue('database', 'database')}")
    engine = create_engine(DATABASE_URL, echo=True)
except KeyError:
    config = Config('config.ini')

class DataBase:
    def __init__(self):
        self.__SQLALCHEMY_DATABASE_URL = (
            f"{config.getValue('database', 'protocol')}://"
            f"{config.getValue('database', 'user')}:" 
            f"{quote_plus(config.getValue('database', 'password'))}@"
            f"{config.getValue('database', 'host')}:" 
            f"{config.getValue('database', 'port')}/"
            f"{config.getValue('database', 'database')}"
        )
        self.engine = create_engine(self.__SQLALCHEMY_DATABASE_URL)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.Base = declarative_base()

    def connect(self):
        try:
            with self.engine.connect() as connection:
                print("Database connection successful!")
        except Exception as e:
            print(f"Database connection failed: {e}")

    def create_tables(self):
        try:
            # Явно указываем метаданные для создания таблиц
            self.Base.metadata.create_all(bind=self.engine)
            print("Tables created successfully!")
        except Exception as e:
            print(f"Error creating tables: {e}")

    def get_session(self):
        """Метод для получения сессии"""
        return self.SessionLocal()

    def get_db(self):
        try:
            yield self.SessionLocal
        finally:
            self.SessionLocal().close()
