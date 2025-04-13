from fastapi import FastAPI
from app.database import engine, Base
from app.routers import employees

app = FastAPI(title="Employee Management")

Base.metadata.create_all(bind=engine)

app.include_router(employees.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}