from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from app.core.config import CONFIG

engine = create_async_engine(CONFIG.SQLALCHEMY_DATABASE_URI)
session_maker = async_sessionmaker(engine,
                                  expire_on_commit=False)

class Base(DeclarativeBase):
    pass

def with_session(func):
    async def wrapper(*args, **kwargs):
        async with session_maker() as session:
            return await func(*args,session=session, **kwargs)
    return wrapper