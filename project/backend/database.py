from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from iniparser import Config

# Чтение конфигурации из файла
config = Config('config.ini')
protocol = config.getValue('database', 'protocol')
user = config.getValue('database', 'user')
password = config.getValue('database', 'password')
host = config.getValue('database', 'host')
port = config.getValue('database', 'port')

class DataBase:
    def __init__(self, database):
        self.__SQLALCHEMY_DATABASE_URL = f"{protocol}://{user}:{password}@{host}:{port}/{database}"
        self.engine = create_engine(self.__SQLALCHEMY_DATABASE_URL)
        self.__sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.Base = declarative_base()

    def connect(self):
        """Проверка подключения к базе данных."""
        try:
            with self.engine.connect() as connection:
                print("Database connection successful!")
        except Exception as e:
            print(f"Database connection failed: {e}")

    def create_tables(self):
        """Создание всех таблиц, определенных в Base."""
        self.Base.metadata.create_all(bind=self.engine)

    def get_session(self):
        """Получение новой сессии для работы с базой данных."""
        return self.__sessionLocal()