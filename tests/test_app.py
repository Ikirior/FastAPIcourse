from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


# Geralmente a função deve ter o nome e o que ela faz
# O root deve retornar status OK e a mensagem Olá Mundo.
# Root é o nome da raiz da URL.
# Ok é o status que indica que a requisição aconteceu com sucesso no HTTP
def test_root_deve_retornar_ok_e_ola_mundo():

    # Cria o cliente de teste
    client = TestClient(app)

    # O cliente faz uma requisição, e nesse ponto é chamado
    # o endereço root com o método GET.
    response = client.get("/")

    # Valida o código de resposta e o status do HTTP
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Olá Mundo!"}
