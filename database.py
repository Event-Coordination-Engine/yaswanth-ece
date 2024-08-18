
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL="postgresql+psycopg2://postgres:yash@localhost/ecedb"

engine= create_engine(URL)
base=declarative_base()
SessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)