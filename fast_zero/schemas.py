from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


# Importante porque esse é o modelo de retorno dos dados
# Não queremos que a senha vaze pela API.
class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr


# Usado para a rota POST
class UserDB(UserSchema):
    id: int


# Usado para a rota GET
class UserList(BaseModel):
    users: list[UserPublic]
