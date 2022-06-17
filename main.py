from fastapi import FastAPI
from routes.user import user
from routes.login import login
from docs import tags_metadata
from fastapi.middleware.cors import CORSMiddleware

# Correr MongoDB desde Docker: docker run -d -p 27017-27019:27017-27019 --name mongodb mongo:5.0.0
app = FastAPI(
    version = 1.0,
    title = "CRUD de Usuarios",
    openapi_tags = tags_metadata,
    description = "Esta es un simple RestAPI que usa FastAPI y MongoDB",
)

@app.get("/", response_model = dict, tags = ["Root"])
def say_hello():
    return {"Hola": "Bienvenido a mi API"}

app.include_router(user)
app.include_router(login)

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"],
    allow_credentials = True,
)