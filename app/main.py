from fastapi import Depends, FastAPI
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.connect import Base, SessionLocal, engine
from app.resources import strings as rte
from app.schema import book as schemas
from app.services.book import BookService

app = FastAPI()


# Dependency function to get a database session
async def get_db():
    async with engine.begin() as conn:
        await conn.run_sync(
            Base.metadata.create_all
        )  # Create database tables if they don't exist
    db = SessionLocal()  # Get a database session
    try:
        yield db  # Yield the database session to the dependent function
    finally:
        await db.close()  # Close the database session after the dependent function finishes


@app.post(
    "/book/",
    name=rte.ADD_BOOK_RTE,
    status_code=201
)
async def create_book(book: schemas.CreateBook, db: AsyncSession = Depends(get_db)):
    """Handler for creating a new book record"""
    return await BookService.add_book(db, book)


@app.delete(
    "/book/",
    name=rte.DELETE_BOOK_RTE,
)
async def delete_book(book: int, db: AsyncSession = Depends(get_db)):
    """Handler for deleting a book record"""
    return await BookService.delete_book(db, book)


@app.get("/book/", name=rte.GET_BOOKS_RTE)
async def get_books(
    req: schemas.GetBooks = Depends(), db: AsyncSession = Depends(get_db)
):
    """Handler for getting book records"""
    return await BookService.get_books(db, req)


@app.put("/book/", name=rte.PUT_BOOKS_RTE)
async def update_book(
    book: int, data: schemas.CreateBook, db: AsyncSession = Depends(get_db)
):
    """Handler for updating a book record"""
    return await BookService.update_book(db, book, data)


@app.post(
    "/review/",
    name=rte.ADD_REVIEW_RTE,
    status_code=201
)
async def create_review(review: schemas.AddReview, db: AsyncSession = Depends(get_db)):
    """Handler for creating a new review record"""
    return await BookService.add_review(db, review)


@app.get(
    "/review/",
    name=rte.GET_REVIEWS_RTE,
)
async def get_reviews(book: int, db: AsyncSession = Depends(get_db)):
    """Handler for getting review records"""
    return await BookService.get_reviews(db, book)


@app.delete(
    "/review/",
    name=rte.DELETE_REVIEW_RTE,
)
async def delete_review(review: int, db: AsyncSession = Depends(get_db)):
    """Handler for deleting a review record"""
    return await BookService.delete_review(db, review)


@app.put(
    "/review/",
    name=rte.UPDATE_REVIEW_RTE,
)
async def update_review(
    review: int, data: schemas.AddReview, db: AsyncSession = Depends(get_db)
):
    """Handler for updating a review record"""
    return await BookService.update_review(db, review, data)
