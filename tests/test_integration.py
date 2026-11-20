from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

##
def test_sumar_integracion():
    respuesta = client.get("/sumar", params={"a": 3, "b": 4})
    assert respuesta.status_code == 200
    assert respuesta.json()["resultado"] == 7


def test_sumar_parametro_invalido():
    respuesta = client.get("/sumar", params={"a": "abc", "b": 4})
    assert respuesta.status_code == 422


def test_promedio_lista_valida():
    respuesta = client.post("/promedio", json={"valores": [2, 4, 6]})
    assert respuesta.status_code == 200
    assert respuesta.json()["promedio"] == 4.0


def test_promedio_lista_vacia():
    respuesta = client.post("/promedio", json={"valores": []})
    assert respuesta.status_code == 400
    assert respuesta.json()["detail"] == "lista vacía"


def test_health():
    respuesta = client.get("/health")
    assert respuesta.status_code == 200
    assert respuesta.json() == {"status": "ok"}


def test_endpoints_conviven():
    assert client.get("/health").json() == {"status": "ok"}
    assert client.get("/sumar", params={"a": 3, "b": 4}).json() == {"resultado": 7}
    assert client.post("/promedio", json={"valores": [2, 4, 6]}).json() == {"promedio": 4.0}
