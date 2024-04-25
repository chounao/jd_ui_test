from page_object.login_page import open_browsers
import pytest

@pytest.fixture(scope='session',autouse=True)
def open_browser():
    open_browsers()

