__author__ = "Narwhale"

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer,create_engine

engine = create_engine("mysql+pymysql://root:1111@192.168.10.1/test",encoding='utf-8',echo = True)

Base = declarative_base()

class user(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    passwd = Column(String(32))

Base.metadata.create_all(engine)