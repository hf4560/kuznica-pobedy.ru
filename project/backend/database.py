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

SQLALCHEMY_DATABASE_URL = f"{protocol}://{user}:{password}@{host}:{port}/volunteer_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

