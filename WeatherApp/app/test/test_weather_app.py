import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
    assert "Weather App" in driver.title  # Updated title check

def test_weather_search(driver):
    driver.get("http://127.0.0.1:5000/")
    search_box = driver.find_element(By.NAME, "user_input")
    search_box.send_keys("new york")
    search_box.send_keys(Keys.RETURN)
    
    driver.implicitly_wait(10)
    page_source = driver.page_source
    try:
        assert "Weather Forecast for New York, NY, United States" in page_source
    except AssertionError:
        print("Page source: ", page_source)
        raise

def test_show_history(driver):
    driver.get("http://127.0.0.1:5000/history")
    assert "Search History" in driver.title
    
    history_items = driver.find_elements(By.TAG_NAME, "li")
    try:
        assert len(history_items) > 0
    except AssertionError:
        print("History items found: ", history_items)
        raise
