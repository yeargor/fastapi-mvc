from abc import ABC, abstractmethod

from sqlalchemy import insert, select

from app.core.db_context import with_session


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self):
        raise NotImplementedError

    @abstractmethod
    async def find_all(self):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    @with_session
    async def add_one(self, session, data: dict) -> int:
        stmt = insert(self.model).values(**data).returning(self.model.id)
        res = await session.execute(stmt)
        await session.commit()
        return res.scalar_one()

    @with_session
    async def find_all(self, session):
        stmt = select(self.model)
        res = await session.execute(stmt)
        res = [row[0].to_read_model() for row in res.all()]
        return res