"""
Запуск приложения
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import api

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
    )

app.include_router(api.router)


@app.get("/")
def home() -> dict[str, str]:
    return {"app status": "OK"}
