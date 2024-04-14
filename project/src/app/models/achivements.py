from pydantic import BaseModel


class AchievementModel(BaseModel):
    """
    Модель данных достижения
    """
    id: int
    achievement_name: str
    points: int
    description: str
