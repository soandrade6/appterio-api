from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import animal_route, procedure_route, research_route, user_route, request_route, auth_route

from app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Appterio API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir aquí los routers
app.include_router(user_route.router)
app.include_router(animal_route.router)
app.include_router(research_route.router)
app.include_router(procedure_route.router)
app.include_router(request_route.router)
app.include_router(auth_route.router)

@app.get("/")
async def root():
    return {"message": "Bienvenido a AppTerio API"}

#Comando para ejecutar la app desde la consola: uvicorn app.main:app --reload

