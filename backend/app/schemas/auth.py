from pydantic import BaseModel

class LoginSchema(BaseModel):
    correo: str
    password: str