from fastapi import FastAPI, Depends, HTTPException
from database import Base,SessionLocal,engine
from models import Users

from sqlalchemy.orm import Session
from pydantic import BaseModel
from fastapi.responses import JSONResponse
Base.metadata.create_all(bind=engine)

app=FastAPI()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

class UserSchema(BaseModel):
    id:str
    name:str
    phoneNumber:str
    dob:str
    gender:str
    class Config:
        orm_model=True

class UserCreateSchema(UserSchema):
    passaword:str

@app.get("/user/{user_id}")
async def get_user():
    return {"Hello": "world"}

@app.post("/api/users",response_model=UserSchema)
def create_users(user:UserCreateSchema, db: Session = Depends(get_db)):
    u=Users(name=user.name, phoneNumber=user.phoneNumber, dob=user.dob, gender=user.gender)
    db.add(u)
    db.commit()
    return u

@app.put("/users{user_id}",response_model=UserSchema)
def update_user(user_id: int, user:UserSchema,db:Session=Depends(get_db)):
    try:
        u=db.query(Users).filter(Users.id==user_id).first()
        u.name=user.name
        u.phoneNumber=user.phoneNumber
        u.dob=user.dob
        u.gender=user.gender
        db.add(u)
        db.commit()
        return u
    except:
        return HTTPException(status_code=404,detail="user not found")

@app.delete("/users{user_id}",response_class=JSONResponse)
def delete_user(user_id:int,db:Session=Depends(get_db)):
    try:
        u=db.query(Users).filter(Users.id==user_id).first()
        db.delete(u)
        return {f"user of id {user_id} has been deleted":True}
    except:
        return HTTPException(status_code=404,detail="user not found")




