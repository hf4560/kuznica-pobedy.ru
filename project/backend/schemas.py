from pydantic import BaseModel
from typing import List, Optional, Dict

class LinkResponse(BaseModel):
    id: int
    text: str
    link_to: Optional[str]
    submenu: Optional[List["LinkResponse"]] = []

    class Config:
        from_attributes = True  # Заменили 'orm_mode' на 'from_attributes'

class ContentData(BaseModel):
    content: Dict