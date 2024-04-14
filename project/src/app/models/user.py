from pydantic import BaseModel
from enum import Enum

class Language(Enum):
    '''Класс, представляющий выбранный язык'''
    russian = 'ru'
    english = 'en'


class UserModel(BaseModel):
    """
    Модель данных пользователя
    """
    id: int
    username: str
    language: Language