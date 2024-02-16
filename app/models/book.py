from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.connect import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    publication_year = Column(Integer)

    review = relationship("Review", backref="reviews")


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    review_text = Column(String)
    rating = Column(Integer)

    book = Column(Integer, ForeignKey("books.id"))
