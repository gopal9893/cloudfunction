from database import Base
from sqlalchemy import Column,String

class Users(Base):
    __tablename__="users"
    id=Column(String,primary_key=True,index=True)
    name=Column(String(50))
    phoneNumber=Column(String(15),unique=True,index=True)
    dob=Column(String(15))
    gender=Column(String(10))

