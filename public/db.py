from config import settings
from sqlalchemy import insert, select
from sqlalchemy import create_engine, text
from models.good import Base, User, Goods

ur_s = settings.POSTGRES_DATABASE_URLS
print(ur_s)
engine_s = create_engine(ur_s, echo=True)

def create_tables():
    Base.metadata.drop_all(bind=engine_s)
    Base.metadata.create_all(bind=engine_s)

def f1():
    with engine_s.connect() as conn:
        answer = conn.execute(text('select * from users;'))
        print(f"answer = {answer.all()}")

def f2():
    with engine_s.connect() as conn:
        answer = conn.execute(text('select * from goods;'))
        print(f"answer = {answer.all()}")

def f1_bilder():
    with engine_s.connect() as conn:
        query = insert(User).values([
            {"name": "Adsdv", "hashed_password": "123545"},
            {"name": "Bdsds", "hashed_password": "123546"}
        ])
        conn.execute(query)
        conn.execute(text('commit;'))
        query = select(User)
        answer = conn.execute(query)
        print(f"answer = {answer.all()}")


def f2_bilder():
    with engine_s.connect() as conn:
        query = insert(Goods).values([
            {"name": "Товар 1", "description": "123545", "price": 50, "nalog": 0},
            {"name": "Товар 2", "description": "125689", "price": 70, "nalog": 10},
        ])
        conn.execute(query)
        conn.execute(text('commit;'))
        query = select(Goods)
        answer = conn.execute(query)
        print(f"answer = {answer.all()}")

create_tables()
f1()
f2()
f1_bilder()
f2_bilder()