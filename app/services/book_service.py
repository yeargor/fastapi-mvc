from app.repositories.base_repository import AbstractRepository
from app.schemas.book_schema import SBookAdd

class BookService:
    def __init__(self, book_repo: AbstractRepository):
        self.book_repo: AbstractRepository = book_repo()

    async def add_book(self, book: SBookAdd):
        book_dict = book.model_dump()
        return await self.book_repo.add_one(data=book_dict)