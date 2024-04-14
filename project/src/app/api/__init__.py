"""
Файл пакета API
"""
from fastapi import APIRouter
from app.api import users_methods

router = APIRouter()
router.include_router(users_methods.router)  
