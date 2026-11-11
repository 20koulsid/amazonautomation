import time

import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setUp(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.in/")
    request.cls.driver = driver
    yield
    time.sleep(4)
    driver.quit()

