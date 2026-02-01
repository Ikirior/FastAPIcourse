from fastapi import FastAPI

app = FastAPI()


@app.get("/")  # Expõe a função a ser servida pelo FastAPI.
# Quando um cliente acessa o endereço de rede com o caminho / a função é
# executada.
def read_root():
    return {"message": "Olá Mundo!"}
