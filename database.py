from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_async_engine('postgresql+asyncpg://postgres:nurshoddeveloper7@localhost/delivery_db', echo=True)


Base = declarative_base()
session = async_sessionmaker()
