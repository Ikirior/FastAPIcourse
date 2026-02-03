from http import HTTPStatus

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message, UserDB, UserList, UserPublic, UserSchema

app = FastAPI()

database = []


@app.get("/", response_class=HTMLResponse)
# Expõe a função a ser servida pelo FastAPI.
# Quando um cliente acessa o endereço de rede com o caminho / a função é
# executada.
def read_root():
    # return {"message": "Olá Mundo!"}
    return """
    <html>
        <head>
            <title> O Olá Mundo! </title>
        </head>
        <body>
            <h1> Olá Mundo </h1>
        </body>
    </html>"""


@app.post("/users/", status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    # O método model_dump converte objetos em dicionário.
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)

    database.append(user_with_id)

    return user_with_id


@app.get("/users/", response_model=UserList)
def read_users():
    return {"users": database}


# Utiliza-se o {user_id} pois a identificação do
# Recurso é dinâmica.
@app.put("/users/{user_id}", response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="User not found"
        )

    user_with_id = UserDB(**user.model_dump(), id=user_id)
    database[user_id - 1] = user_with_id

    return user_with_id


@app.delete("/users/{user_id}", response_model=Message)
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail="User not found"
        )

    del database[user_id - 1]
    return {"message": "User deleted"}
