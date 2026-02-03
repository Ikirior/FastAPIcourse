import pytest
from fastapi.testclient import TestClient

from fast_zero.app import app


# Permite evitar a repetição da linha TestClient
# No arquivo de testes.
@pytest.fixture
def client():
    return TestClient(app)
