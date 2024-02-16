from typing import Optional

from pydantic import BaseModel, conint


class CreateBook(BaseModel):
    title: str
    author: str
    publication_year: int


class AddReview(BaseModel):
    review_text: str
    rating: conint(gt=0, lt=6)
    book: int


class GetBooks(BaseModel):
    author: Optional[str]
    publication_year: Optional[int]
