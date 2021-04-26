import shutil
import subprocess
import time
from pathlib import Path
  
import pytest
import redis
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
#from tenacity import retry, stop_after_delay

from fitlib.adapters.orm import metadata, start_mappers
from fitlib import config

pytest.register_assert_rewrite("tests.e2e.api_client")


@pytest.fixture
def in_memory_sqlite_db():
    engine = create_engine("sqlite:///:memory:")
    metadata.create_all(engine)
    return engine


@pytest.fixture
def sqlite_session_factory(in_memory_sqlite_db):
    yield sessionmaker(bind=in_memory_sqlite_db)


@pytest.fixture
def mappers():
    start_mappers()
    yield
    clear_mappers()

@pytest.fixture(scope="session")
def file_sqlite_db():
    engine = create_engine(config.get_sqlite_file_url(), isolation_level="SERIALIZABLE")
    wait_for_sqlite_to_come_up(engine)
    metadata.create_all(engine)
    return engine   


@pytest.fixture(scope="session")
def postgres_db():
    engine = create_engine(config.get_postgres_uri(), isolation_level="SERIALIZABLE")
    wait_for_postgres_to_come_up(engine)
    metadata.create_all(engine)
    return engine


@pytest.fixture
def postgres_session_factory(postgres_db):
    yield sessionmaker(bind=postgres_db)


@pytest.fixture
def postgres_session(postgres_session_factory):
    return postgres_session_factory()
