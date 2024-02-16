



SAMPLE_BOOK = {
  "id":3,
  "title": "test book",
  "author": "test author",
  "publication_year": 2022
}

SAMPLE_REVIEW = {
  "id":3,
  "review_text": "test_review",
  "rating": 3,
  "book": 3
}

REQ_1 =SAMPLE_BOOK

DB_RES_1 =SAMPLE_BOOK

RES_1 =SAMPLE_BOOK


REQ_2 = {
  "title": 233,
  "publication_year": 2022
}

DB_RES_2 = {}

RES_2 = {'detail': [{'loc': ['body', 'author'], 'msg': 'field required', 'type': 'value_error.missing'}]}


REQ_3 = SAMPLE_REVIEW

DB_RES_3 = SAMPLE_REVIEW

RES_3 = SAMPLE_REVIEW

REQ_4 = {
  "review_text": "test_review",
  "rating": 7,
  "book": 1
}

DB_RES_4 = {
}

RES_4 = {'detail': [{'loc': ['body', 'rating'], 'msg': 'ensure this value is less than 6', 'type': 'value_error.number.not_lt', 'ctx': {'limit_value': 6}}]}



REQ_5 = {
}

DB_RES_5 = SAMPLE_BOOK

RES_5 = SAMPLE_BOOK

REQ_6 = {
  "book":3
}

DB_RES_6 = SAMPLE_BOOK

RES_6 = SAMPLE_BOOK

REQ_7 = {
  "params":{"book":3},
  "body":{
    "title": "test book",
  "author": "test author",
  "publication_year": 2022
  }
}

DB_RES_7 = SAMPLE_BOOK

RES_7 = SAMPLE_BOOK


REQ_8= {
  "params":{"review":3},
  "body":SAMPLE_REVIEW
}

DB_RES_8= SAMPLE_REVIEW

RES_8= SAMPLE_REVIEW

REQ_9= {
  "params":{"review":3},
  "body":SAMPLE_REVIEW
}

DB_RES_9= {}

RES_9= {'detail': 'Review not found'}


REQ_10 = {
  "params":{"book":3},
  "body": SAMPLE_BOOK
}

DB_RES_10 = None

RES_10 = {'detail': 'Book not found'}


REQ_11 = {
  "params":{"book":3},
}

DB_RES_11 = None

RES_11 = None

REQ_12 = {
  "params":{"book":3},
}

DB_RES_12 = None

RES_12 =  {'detail': 'Book not found'}

REQ_13 = {
  "params":{"review":3},
}

DB_RES_13 = None

RES_13 = None

REQ_14 = {
  "params":{"review":3},
}

DB_RES_14 = None

RES_14 =  {'detail': 'Review not found'}