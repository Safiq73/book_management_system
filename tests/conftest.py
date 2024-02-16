import warnings

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pytest import fixture
from app.main import app as application
from app.main import get_db

class TestSession:
    
    async def close(self):
        pass
    
    async def get(self, *args, **kwargs):
        pass

def override_get_db():
    try:
        db = TestSession()
        yield db
    finally:
        db.close()


application.dependency_overrides[get_db] = override_get_db

@fixture(scope="function")
async def test_client():
    client = TestClient(application)
    return client


@pytest.fixture(scope="function")
def app() -> FastAPI:
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    return application