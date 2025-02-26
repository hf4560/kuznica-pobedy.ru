from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from iniparser import Config

config = Config('config.ini')
protocol = config.getValue('database', 'protocol')
user = config.getValue('database', 'user')
password = config.getValue('database', 'password')
host = config.getValue('database', 'host')
port = config.getValue('database', 'port')



class DataBase(create_engine):
    def __init__(self, database):
        self.__SQLALCHEMY_DATABASE_URL = f"{protocol}://{user}:{password}@{host}:{port}/{database}"
        super().__init__(self.__SQLALCHEMY_DATABASE_URL)
        self.connect()
        try:
            with self.connect() as connection:
                print("Database connection successful!")
        except Exception as e:
            print(f"Database connection failed: {e}")
        self.__sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self)
        self.__base = declarative_base()



