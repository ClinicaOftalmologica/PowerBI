from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine = create_engine("postgresql://postgres:postgres123@localhost:5432/python_sw")
Session = sessionmaker(bind=engine)
