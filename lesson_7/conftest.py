import time
import pytest


def pytest_addoption(parser):
    parser.addoption("--url", action="store", type=str,
                     default="https://ya.ru", help="URL to test")
    parser.addoption("--status_code", action="store", type=int,
                     default=200, help="Expected status code")


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")


@pytest.fixture(autouse=True)
def timer(request):
    start_time = time.time()
    yield
    end_time = time.time()
    test_duration = end_time - start_time
    print(f"Test {request.node.name} took {test_duration:.5f} seconds")
