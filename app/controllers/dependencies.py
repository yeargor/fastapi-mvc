from app.repositories.book_repository import BookRepository
from app.services.book_service import BookService


def book_service():
    return BookService(BookRepository)