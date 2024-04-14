"""
Описание API для загрузки и выгрузки файлов
"""
from typing import List, Any
from fastapi import APIRouter, Depends
from app.services.DB_services import DBService

router = APIRouter(
    prefix="/DB",
    tags=['DB_API']
)


@router.get('/home/')
def homeapi( service: DBService = Depends()):
    return service.home()


