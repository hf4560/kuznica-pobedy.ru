from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import HeaderLink
from schemas import LinkResponse
from database import DataBase

router = APIRouter()
# Инициализация базы данных
db_instance = DataBase()
db_instance.connect()
db_instance.create_tables()

# Dependency для получения сессии
def get_db():
    db = db_instance.get_session()
    try:
        yield db
    finally:
        db.close()

@router.get("/api/headerlinks", response_model=list[LinkResponse])
async def get_links(db: Session = Depends(get_db)):
    # Получаем все родительские ссылки (где parent_id == None)
    root_links = db.query(HeaderLink).filter(HeaderLink.parent_id == None).all()

    def get_submenu(link):
        # Загружаем подменю для текущей ссылки, если оно есть
        submenu = db.query(HeaderLink).filter(HeaderLink.parent_id == link.id).all()
        return LinkResponse(
            id=link.id,
            text=link.text,
            link_to=link.link_to,
            submenu=[get_submenu(sub) for sub in submenu] if submenu else []
        )

    # Возвращаем все родительские ссылки с подменю
    return [get_submenu(link) for link in root_links]
