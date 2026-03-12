from pydantic import BaseModel , Field, EmailStr, ConfigDict
from typing import Optional


class Address(BaseModel):
    city: str = Field(...,min_length =3)
    pincode:str = Field(...,pattern=r"^\d{6}$")

    model_config=ConfigDict(validate_assignment=True)

class user(BaseModel):
    user_id: int
    name: str
    email: EmailStr
    age: int = Field(..., ge=18)
    address: Address
    is_premium: Optional[bool] = False

    model_config=ConfigDict(validate_assignment=True)


data = {
    "user_id" : "345",
    "name" : "Mike",
    "email" : "mike@mike.com",
    "age": 43,
    "address":
        {
            "city": "Gotham",
            "pincode":"342346"
        },
    "is_premium":True
}

user_instance = user(**data)
print(user_instance.address.city)