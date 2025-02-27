from database import DataBase

def initialize_database():
    db = DataBase()
    db.connect()
    db.create_tables()

if __name__ == "__main__":
    initialize_database()