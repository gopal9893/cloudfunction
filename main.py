from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class User(BaseModel):
    phoneNumber: str
    fullName: str
    email: str
    dob: str
    gender: str

@app.post("/user/")
def create_user(user: User):
    return user

@app.get("/user/{user_id}")
async def get_user():
    return {"Hello": "world"}










