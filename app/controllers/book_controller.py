from typing import Annotated

from fastapi import APIRouter, Depends

from app.controllers.dependencies import book_service
from app.schemas.book_schema import SBookAdd
from app.services.book_service import BookService

router = APIRouter(prefix="/test")

@router.post("")
async def post_book(
        book: SBookAdd,
        task_service: Annotated[BookService, Depends(book_service)]
):
    book_id = await task_service.add_book(book)
    return book_id
