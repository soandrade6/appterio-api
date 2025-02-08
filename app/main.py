from fastapi import FastAPI
from app.routes import users, animals
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Appterio API")

# Incluir aquí los routers
app.include_router(users.router)
app.include_router(animals.router)

#Comando para ejecutar la app desde la consola: uvicorn app.main:app --reload

