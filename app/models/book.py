from sqlalchemy.orm import Mapped, mapped_column

from app.core.db_context import Base


class Book(Base):
    __tablename__ = 'book'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str | None]
