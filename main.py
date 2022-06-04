from fastapi import FastAPI
from routes.user import user
from docs import tags_metadata
from fastapi.middleware.cors import CORSMiddleware

# Correr MongoDB desde Docker: docker run -d -p 27017-27019:27017-27019 --name mongodb mongo:5.0.0
app = FastAPI(
    title = "CRUD de Usuarios",
    description = "Esta es un simple RestAPI que usa FastAPI y MongoDB",
    version = 1.0,
    openapi_tags = tags_metadata
)

@app.get("/", response_model = dict, tags = ["Root"])
def say_hello():
    return {"Hola": "Bienvenido a mi API"}

app.include_router(user)

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"],
    allow_credentials = True,
)