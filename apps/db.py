import sqlalchemy
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

from settings.base import SQLALCHEMY_DATABASE_URI

engine = create_async_engine(url=SQLALCHEMY_DATABASE_URI, future=True, echo=True)

Session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()
Base.metadata.bind = engine


async def get_sql_db():
    async with Session() as session:
        yield session
