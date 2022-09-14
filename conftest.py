#conftest.py используется для хранения общих фикстур, которые используются для всего проетка

from selene.support.shared import browser
import pytest


@pytest.fixture(scope="session", autouse=True)
def seting_window_browser():
    browser.config.window_height = 480
    browser.config.window_width = 640
    yield
    browser.close()
