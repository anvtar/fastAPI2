#import asyncio
#from sqlalchemy.ext.asyncio import create_async_engine
from config import settings
from sqlalchemy import create_engine, text
from models.good import Base
#ur_p = "postgresql+asyncpg://postgres:0000@localhost:5432/test"
ur_s = settings.POSTGRES_DATABASE_URLS
ur_a = settings.POSTGRES_DATABASE_URLA
print(ur_s)
engine_s = create_async_engine(ur_p, echo=True)
async def f():
    async with engine.connect() as conn:
        answer = await conn.execute(text("select version()"))
        print(f"answer = {answer.all()}")
asyncio.run(f())
