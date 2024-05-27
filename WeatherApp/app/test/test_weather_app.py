import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="module")
def driver():
    # Setup Chrome WebDriver
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


def test_home_page(driver):
    driver.get("http://127.0.0.1:5000/")
    assert "Weather App" in driver.title


def test_weather_search(driver):
    driver.get("http://127.0.0.1:5000/")
    search_box = driver.find_element_by_name("user_input")
    search_box.send_keys("New York")
    search_box.submit()
    assert "Weather Forecast for New York" in driver.page_source


def test_show_history(driver):
    driver.get("http://127.0.0.1:5000/history")
    assert "Search History" in driver.title
