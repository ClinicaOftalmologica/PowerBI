from sqlalchemy import Column,String,Integer,true
from db import Base,engine

class Usuario(Base):
    __tablename__ = "usuarios"
    id =Column(Integer,autoincrement=true,primary_key=true)
    username=Column(String(70),unique=true)
    password = Column(String(40))


Base.metadata.create_all(engine)