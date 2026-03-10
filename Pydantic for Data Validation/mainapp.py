from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()

class UserRegister(BaseModel):
    username: str = Field(..., min_length=5)
    email: EmailStr
    age: int = Field(...,ge=18)


@app.post("/register")
async def register_usr(user: UserRegister):
    return {"message": "user registered successfully", "user": user}
