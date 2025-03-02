from sqlalchemy.orm import Session
from models import HeaderLink  # Импорт модели HeaderLink
from database import DataBase
from iniparser import Config

config = Config('config.ini')

# Инициализация базы данных
db_instance = DataBase()
db_instance.connect()
db_instance.create_tables()

# Получение сессии базы данных
def get_db():
    db = db_instance.get_session()
    return db


def add_link(db, text, link_to, parent_id=None):
    link = HeaderLink(text=text, link_to=link_to, parent_id=parent_id)
    db.add(link)  # добавляем ссылку в базу данных
    db.commit()  # фиксируем изменения
    db.refresh(link)  # обновляем объект
    return link


def fill_table(db: Session):
    """Функция для заполнения таблицы нужными данными"""

    # Добавляем главные ссылки
    news_link = add_link(db, 'Новости', '/news')
    volunteers_link = add_link(db, 'Волонтерам', '')
    defenders_link = add_link(db, 'Защитникам', '/defenders')
    about_link = add_link(db, 'О нас', '')
    contact_link = add_link(db, 'Связаться', '/contact')
    support_link = add_link(db, 'Поддержать нас', '/support')


    # Добавляем подменю для "О нас"
    add_link(db, 'Структура и миссия', '/about/structure', parent_id=about_link.id)
    add_link(db, 'Контакты', '/about/contacts', parent_id=about_link.id)
    add_link(db, 'Отзывы', '/about/reviews', parent_id=about_link.id)

    # Добавляем подменю для "Волонтерам"
    add_link(db, 'Новым волонтерам', '/volunteers/new', parent_id=volunteers_link.id)
    add_link(db, 'Инструкции', '/volunteers/instructions', parent_id=volunteers_link.id)


if __name__ == "__main__":
    db = get_db()  # Получаем сессию
    fill_table(db)  # Заполняем таблицу
    db.close()  # Закрываем сессию
