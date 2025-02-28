from fastapi import FastAPI
from app.routes import animal_route, procedure_route, research_route, user_route
from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Appterio API")

# Incluir aquí los routers
app.include_router(user_route.router)
app.include_router(animal_route.router)
app.include_router(research_route.router)
app.include_router(procedure_route.router)

#Comando para ejecutar la app desde la consola: uvicorn app.main:app --reload

