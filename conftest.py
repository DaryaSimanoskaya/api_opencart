import os
import random
import time
from datetime import datetime, timezone

import pytest
from config.http_client import HttpClient

import allure
import logging


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    item.logger = logger

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_call(item):
    if hasattr(item, 'logger'):
        logger = item.logger
        logger.info(f"Running test: {item.name}")


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_teardown(item):
    if hasattr(item, 'logger'):
        logger = item.logger
        logger.info(f"Finished test: {item.name}")

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_logreport(report):
    if report.failed and hasattr(report, 'longrepr'):
        allure.attach(str(report.longrepr), name="Error Log", attachment_type=allure.attachment_type.TEXT)


def pytest_addoption(parser):
    parser.addoption("--url", default="http://192.168.0.108:8080/index.php?route=", help="BaseUrl for api_tests API")
    parser.addoption("--username", default="MyAPI", help="username for opencart api")
    parser.addoption("--key", default="KbuOvLXY3AzdURPCXDpp7UEKpIbdKdxteGTiik5i4rPbr0Nc0aAoUNtvUMbau3pEw6KceURIScG0rnqdiJJOR2BsAqyCyWpVsvvWZw4HYtiAPHA0EovyROCmMJjRUVRPT51LUtZr8b0Ru6isx0GPfl0ZgjrrEVh3R6yF8wNAJ5nYTq5bXdegISdW7CLYme1Pns8TnRh00g4u5fHeEgg1SKfBl7yYRwnuADPSSx7wDyonbw20MndNfske1hSSivFB", help="key for opencart api")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="session")
def username(request):
    return request.config.getoption("--username")


@pytest.fixture(scope="session")
def key(request):
    return request.config.getoption("--key")


@pytest.fixture(scope="session")
def client(base_url, username, key):
    client = HttpClient(base_url=base_url, username=username, key=key)
    yield client

