"""
This module contains string constants used as route names (RTE) for various API endpoints.
These constants are used to specify the route names when defining FastAPI endpoints, and are
also used in generating error messages and logging statements.
"""
INTERNAL_SERVER_ERROR = "Internal Server Error"


ADD_BOOK_RTE = "Post:Add Book"
DELETE_BOOK_RTE = "Delete:delete Book"
DELETE_REVIEW_RTE = "Delete:delete Review"
UPDATE_REVIEW_RTE = "PUT:Update Review"
GET_BOOKS_RTE = "Get:Fetch Books"
PUT_BOOKS_RTE = "Put:Update Book"
GET_REVIEWS_RTE = "Get:Fetch Reviews"
ADD_REVIEW_RTE = "Post:Add Review"
