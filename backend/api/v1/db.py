import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USER_NAME = 'root'
USER = 'root'
PASSWORD = 'rootpassword'
HOST = 'db'
PORT = 3306
DATABASE = 'memorandum'

SQL_ALCEMY_DATABASE_URL = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?charset=utf8'

engine = create_engine(SQL_ALCEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
