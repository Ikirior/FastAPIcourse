from http import HTTPStatus


# Geralmente a função deve ter o nome e o que ela faz
# O root deve retornar status OK e a mensagem Olá Mundo.
# Root é o nome da raiz da URL.
# Ok é o status que indica que a requisição aconteceu com sucesso no HTTP
def test_root_deve_retornar_ok_e_ola_mundo(client):

    # O cliente faz uma requisição, e nesse ponto é chamado
    # o endereço root com o método GET.
    response = client.get("/")

    # Valida o código de resposta e o status do HTTP
    assert response.status_code == HTTPStatus.OK
    assert response.text


def test_create_user(client):

    response = client.post(
        "/users/",
        json={
            "username": "alice",
            "email": "alice@example.com",
            "password": "secret",
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "username": "alice",
        "email": "alice@example.com",
        "id": 1,
    }


def test_read_users(client):
    response = client.get("/users/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {
                "username": "alice",
                "email": "alice@example.com",
                "id": 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        "/users/1",
        json={
            "username": "bob",
            "email": "bob@example.com",
            "password": "mynewpassword",
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "username": "bob",
        "email": "bob@example.com",
        "id": 1,
    }


def test_delete_user(client):

    response = client.delete("/users/1")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "User deleted"}
