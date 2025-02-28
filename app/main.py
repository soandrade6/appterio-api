from fastapi import FastAPI
from app.routes import animal, procedure_routes, user, research
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Appterio API")

# Incluir aquí los routers
app.include_router(user.router)
app.include_router(animal.router)
app.include_router(research.router)
app.include_router(procedure_routes.router)

#Comando para ejecutar la app desde la consola: uvicorn app.main:app --reload

