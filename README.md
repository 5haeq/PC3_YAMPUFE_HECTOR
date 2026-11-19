# PC3 — API FastAPI

Práctica calificada 3: construcción incremental de una API con FastAPI, pruebas de integración y estilo cliente-servidor.

**Alumno:** Yampufe Pau, Héctor Alonso

## Estructura

```
PC3_YAMPUFE_HECTOR/
├── app/
│   ├── __init__.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_integration.py
├── requirements.txt
└── run.sh
```

## Endpoints

| Método | Ruta        | Descripción                              |
|--------|-------------|------------------------------------------|
| GET    | `/health`   | Estado del servicio: `{"status": "ok"}`  |
| GET    | `/sumar`    | Suma dos enteros: `?a=3&b=4`             |
| POST   | `/promedio` | Promedio de una lista JSON de números    |

Ejemplos:

```bash
curl "http://localhost:8080/sumar?a=3&b=4"
# {"resultado":7}

curl -X POST "http://localhost:8080/promedio" \
  -H "Content-Type: application/json" \
  -d '{"valores": [2, 4, 6]}'
# {"promedio":4.0}
```

## Instalación

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ejecutar en el puerto 8080

```bash
./run.sh
```

o directamente:

```bash
uvicorn app.main:app --reload --port 8080
```

La documentación interactiva queda en <http://localhost:8080/docs>.

## Pruebas

```bash
pytest tests/ -v
```
