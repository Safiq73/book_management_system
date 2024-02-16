import pytest
from fastapi import FastAPI
from starlette.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST,HTTP_201_CREATED,HTTP_404_NOT_FOUND,
                              HTTP_422_UNPROCESSABLE_ENTITY)
from .helper import *
from fastapi.testclient import TestClient
from app.resources import strings as rte

@pytest.mark.parametrize(
    "request_body, db_response, expected, response_json",
    [
        (
            REQ_1,
            DB_RES_1,
            HTTP_201_CREATED,
            RES_1,
        ),
        (
            REQ_2,
            DB_RES_2,
            HTTP_422_UNPROCESSABLE_ENTITY,
            RES_2,
        ),
    ],
)
def test_create_book(
    app: FastAPI,
    test_client: TestClient,
    request_body,
    db_response,
    expected,
    response_json,
    mocker,
):
    mocker.patch(
        "app.repositories.book.BookRepository.create_book",
        return_value=db_response,
    )
    
    response = test_client.post(
        app.url_path_for(rte.ADD_BOOK_RTE),
        json=request_body,
    )
    test_response_json = response.json()
    # import pdb; pdb.set_trace()
    assert response.status_code == expected
    assert test_response_json == response_json


@pytest.mark.parametrize(
    "request_body, db_response, expected, response_json",
    [
        (
            REQ_3,
            DB_RES_3,
            HTTP_201_CREATED,
            RES_3,
        ),
        (
            REQ_4,
            DB_RES_4,
            HTTP_422_UNPROCESSABLE_ENTITY,
            RES_4,
        ),
    ],
)
def test_add_review(
    app: FastAPI,
    test_client: TestClient,
    request_body,
    db_response,
    expected,
    response_json,
    mocker,
):
    mocker.patch(
        "app.repositories.book.BookRepository.create_review",
        return_value=db_response,
    )
    
    response = test_client.post(
        app.url_path_for(rte.ADD_REVIEW_RTE),
        json=request_body,
    )
    test_response_json = response.json()
    assert response.status_code == expected
    assert test_response_json == response_json


@pytest.mark.parametrize(
    "request_body, db_response, expected, response_json",
    [
        (
            {},
            DB_RES_5,
            HTTP_200_OK,
            RES_5,
        )
    ],
)
def test_get_book(
    app: FastAPI,
    test_client: TestClient,
    request_body,
    db_response,
    expected,
    response_json,
    mocker,
):
    mocker.patch(
        "app.repositories.book.BookRepository.get_books",
        return_value=db_response,
    )
    
    response = test_client.get(
        app.url_path_for(rte.GET_BOOKS_RTE),
    )
    test_response_json = response.json()
    assert response.status_code == expected
    assert test_response_json == response_json

@pytest.mark.parametrize(
    "request_body, db_response, expected, response_json",
    [
        (
            REQ_6,
            DB_RES_6,
            HTTP_200_OK,
            RES_6,
        )
    ],
)
def test_get_review(
    app: FastAPI,
    test_client: TestClient,
    request_body,
    db_response,
    expected,
    response_json,
    mocker,
):
    mocker.patch(
        "app.repositories.book.BookRepository.get_reviews_by_book",
        return_value=db_response,
    )
    response = test_client.get(
        app.url_path_for(rte.GET_REVIEWS_RTE),
        params=request_body,
    )
    test_response_json = response.json()
    assert response.status_code == expected
    assert test_response_json == response_json

@pytest.mark.parametrize(
    "request_body, db_response, expected, response_json",
    [
        (
            REQ_7,
            DB_RES_7,
            HTTP_200_OK,
            RES_7,
        )
    ],
)
def test_update_book(
    app: FastAPI,
    test_client: TestClient,
    request_body,
    db_response,
    expected,
    response_json,
    mocker,
):
    mocker.patch(
        "app.repositories.book.BookRepository.update_book",
        return_value=db_response,
    )
    response = test_client.put(
        app.url_path_for(rte.PUT_BOOKS_RTE),
        params=request_body.get("params"),
        json=request_body.get("body"),
    )
    test_response_json = response.json()
    assert response.status_code == expected
    assert test_response_json == response_json


@pytest.mark.parametrize(
    "request_body, db_response, expected, response_json",
    [
        (
            REQ_7,
            DB_RES_7,
            HTTP_200_OK,
            RES_7,
        ),
        (
            REQ_10,
            DB_RES_10,
            HTTP_404_NOT_FOUND,
            RES_10,
        ),
    ],
)
def test_update_book(
    app: FastAPI,
    test_client: TestClient,
    request_body,
    db_response,
    expected,
    response_json,
    mocker,
):
    if expected not in [HTTP_404_NOT_FOUND]:
        mocker.patch(
            "app.repositories.book.BookRepository.update_book",
            return_value=db_response,
        )
    else:
        mocker.patch(
            "sqlalchemy.ext.asyncio.AsyncSession.get",
            return_value=db_response,
        )
    response = test_client.put(
        app.url_path_for(rte.PUT_BOOKS_RTE),
        params=request_body.get("params"),
        json=request_body.get("body"),
    )
    test_response_json = response.json()
    assert response.status_code == expected
    assert test_response_json == response_json

@pytest.mark.parametrize(
    "request_body, db_response, expected, response_json",
    [
        (
            REQ_8,
            DB_RES_8,
            HTTP_200_OK,
            RES_8,
        ),
        (
            REQ_9,
            DB_RES_9,
            HTTP_404_NOT_FOUND,
            RES_9,
        ),
    ],
)
def test_update_review(
    app: FastAPI,
    test_client: TestClient,
    request_body,
    db_response,
    expected,
    response_json,
    mocker,
):
    if expected not in [HTTP_404_NOT_FOUND]:
        mocker.patch(
            "app.repositories.book.BookRepository.update_review",
            return_value=db_response,
        )
    else:
        mocker.patch(
            "sqlalchemy.ext.asyncio.AsyncSession.get",
            return_value=db_response,
        )
    response = test_client.put(
        app.url_path_for(rte.UPDATE_REVIEW_RTE),
        params=request_body.get("params"),
        json=request_body.get("body"),
    )
    test_response_json = response.json()
    assert response.status_code == expected
    assert test_response_json == response_json

@pytest.mark.parametrize(
    "request_body, db_response, expected, response_json",
    [
        (
            REQ_11,
            DB_RES_11,
            HTTP_200_OK,
            RES_11,
        ),
        (
            REQ_12,
            DB_RES_12,
            HTTP_404_NOT_FOUND,
            RES_12,
        ),
    ],
)
def test_delete_book(
    app: FastAPI,
    test_client: TestClient,
    request_body,
    db_response,
    expected,
    response_json,
    mocker,
):
    if expected not in [HTTP_404_NOT_FOUND]:
        mocker.patch(
            "app.repositories.book.BookRepository.delete_book",
            return_value=db_response,
        )
    else:
        mocker.patch(
            "sqlalchemy.ext.asyncio.AsyncSession.get",
            return_value=db_response,
        )
    response = test_client.delete(
        app.url_path_for(rte.DELETE_BOOK_RTE),
        params=request_body.get("params"),
    )
    test_response_json = response.json()
    assert response.status_code == expected
    assert test_response_json == response_json



@pytest.mark.parametrize(
    "request_body, db_response, expected, response_json",
    [
        (
            REQ_13,
            DB_RES_13,
            HTTP_200_OK,
            RES_13,
        ),
        (
            REQ_14,
            DB_RES_14,
            HTTP_404_NOT_FOUND,
            RES_14,
        ),
    ],
)
def test_delete_review(
    app: FastAPI,
    test_client: TestClient,
    request_body,
    db_response,
    expected,
    response_json,
    mocker,
):
    if expected not in [HTTP_404_NOT_FOUND]:
        mocker.patch(
            "app.repositories.book.BookRepository.delete_review",
            return_value=db_response,
        )
    else:
        mocker.patch(
            "sqlalchemy.ext.asyncio.AsyncSession.get",
            return_value=db_response,
        )
    response = test_client.delete(
        app.url_path_for(rte.DELETE_REVIEW_RTE),
        params=request_body.get("params"),
    )
    test_response_json = response.json()
    assert response.status_code == expected
    assert test_response_json == response_json
