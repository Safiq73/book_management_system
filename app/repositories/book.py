from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.book import Book, Review
from app.schema.book import AddReview, CreateBook

class BookRepository:
    
    @staticmethod
    async def create_book(db: AsyncSession, book: CreateBook):
        """
        Creates a new book entry in the database.

        Parameters:
        - db (AsyncSession): The asynchronous database session.
        - book (CreateBook): The book data to be created.

        Returns:
        - Book: The created book object.
        """
        book = Book(**book.dict())
        db.add(book)
        await db.commit()
        await db.refresh(book)
        return book


    @staticmethod
    async def create_review(db: AsyncSession, review: AddReview):
        """
        Creates a new review entry in the database.

        Parameters:
        - db (AsyncSession): The asynchronous database session.
        - review (AddReview): The review data to be created.

        Returns:
        - Review: The created review object.
        """
        review = Review(**review.dict())
        db.add(review)
        await db.commit()
        await db.refresh(review)
        return review


    @staticmethod
    async def get_books(db: AsyncSession, author: int = None, publication_year: int = None):
        """
        Retrieves books from the database based on optional filtering criteria.

        Parameters:
        - db (AsyncSession): The asynchronous database session.
        - author (int, optional): The author ID to filter books by.
        - publication_year (int, optional): The publication year to filter books by.

        Returns:
        - List[Book]: A list of book objects matching the filter criteria.
        """
        query = select(Book)
        if author:
            query = query.filter(Book.author == author)
        if publication_year:
            query = query.filter(Book.publication_year == publication_year)
        result = await db.execute(query)
        return result.scalars().all()


    @staticmethod
    async def get_reviews_by_book(db: AsyncSession, book: int):
        """
        Retrieves reviews from the database for a given book.

        Parameters:
        - db (AsyncSession): The asynchronous database session.
        - book (int): The ID of the book to retrieve reviews for.

        Returns:
        - List[Review]: A list of review objects for the specified book.
        """
        async with db.begin():
            query = select(Review).filter(Review.book == book)
            result = await db.execute(query)
            return result.scalars().all()


    @staticmethod
    async def delete_book(db: AsyncSession, book: int):
        """
        Deletes a book entry from the database.

        Parameters:
        - db (AsyncSession): The asynchronous database session.
        - book (int): The ID of the book to delete.

        Raises:
        - HTTPException: If the book is not found in the database.
        """
        book = await db.get(Book, book)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        await db.delete(book)
        await db.commit()


    @staticmethod
    async def delete_review(db: AsyncSession, review: int):
        """
        Deletes a review entry from the database.

        Parameters:
        - db (AsyncSession): The asynchronous database session.
        - review (int): The ID of the review to delete.

        Raises:
        - HTTPException: If the review is not found in the database.
        """
        review = await db.get(Review, review)
        if not review:
            raise HTTPException(status_code=404, detail="Review not found")
        await db.delete(review)
        await db.commit()


    @staticmethod
    async def update_book(db: AsyncSession, book: int, data: CreateBook):
        """
        Updates an existing book entry in the database.

        Parameters:
        - db (AsyncSession): The asynchronous database session.
        - book (int): The ID of the book to update.
        - data (CreateBook): The updated book data.

        Returns:
        - Book: The updated book object.

        Raises:
        - HTTPException: If the book is not found in the database.
        """
        book = await db.get(Book, book)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        for key, value in data.dict().items():
            setattr(book, key, value)
        await db.commit()
        await db.refresh(book)
        return book


    @staticmethod
    async def update_review(db: AsyncSession, review: int, data: AddReview):
        """
        Updates an existing review entry in the database.

        Parameters:
        - db (AsyncSession): The asynchronous database session.
        - review (int): The ID of the review to update.
        - data (AddReview): The updated review data.

        Returns:
        - Review: The updated review object.

        Raises:
        - HTTPException: If the review is not found in the database.
        """
        review = await db.get(Review, review)
        if not review:
            raise HTTPException(status_code=404, detail="Review not found")
        for key, value in data.dict().items():
            setattr(review, key, value)
        await db.commit()
        await db.refresh(review)
        return review
