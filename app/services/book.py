import asyncio

from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.book import BookRepository
from app.schema import book as schemas
from app.services.email import EmailService

class BookService:
    @staticmethod
    async def add_book(db: AsyncSession, book: schemas.CreateBook):
        """
        Adds a new book to the database.
        """
        data = await BookRepository.create_book(db, book)
        return data


    @staticmethod
    async def add_review(db: AsyncSession, review: schemas.CreateBook):
        """
        Adds a new review to the database and sends an email notification asynchronously.
        """
        data = await BookRepository.create_review(db, review)
        asyncio.create_task(
            EmailService.send_email("test@test.com", "test@testing.com", "123")
        )
        return data

    @staticmethod
    async def get_books(db: AsyncSession, req: schemas.GetBooks):
        """
        Retrieves books from the database based on optional filtering criteria.
        """
        return await BookRepository.get_books(db, req.author, req.publication_year)

    @staticmethod
    async def get_reviews(db: AsyncSession, book: int):
        """
        Retrieves reviews for a given book from the database.
        """
        return await BookRepository.get_reviews_by_book(db, book)

    @staticmethod
    async def delete_book(db: AsyncSession, book: int):
        """
        Deletes a book from the database.
        """
        return await BookRepository.delete_book(db, book)

    @staticmethod
    async def update_book(db: AsyncSession, book: int, data: schemas.CreateBook):
        """
        Updates an existing book entry in the database.
        """
        return await BookRepository.update_book(db, book, data)

    @staticmethod
    async def delete_review(db: AsyncSession, review: int):
        """
        Deletes a review from the database.
        """
        return await BookRepository.delete_review(db, review)

    @staticmethod
    async def update_review(db: AsyncSession, review: int, data: int):
        """
        Updates an existing review entry in the database.
        """
        return await BookRepository.update_review(db, review, data)
