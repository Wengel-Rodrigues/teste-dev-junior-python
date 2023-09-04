from fastapi import FastAPI
from database.db import init_db
from app.routes import router

app = FastAPI()

# Evento para rodar no startup
@app.on_event("startup")
def startup_event():
    init_db()

app.include_router(router)

    