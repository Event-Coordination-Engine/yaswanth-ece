from database import base
from sqlalchemy.orm import relationship
from sqlalchemy import Column,Integer,String

class user(Base):
    __tablename__="user"
    
    
    
user_id=Column(Integer,primary_key=True)
first_name=Column(String,nullable=False)
last_name=column(string,nullable=True)
email=column(string,nullable=False)
password=column(String,nullable=False)