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
    # Wait for the response and check for the expected text
    driver.implicitly_wait(10)
    assert "Weather Forecast for New York, NY, United States" in driver.page_source  # Ensure this text appears in the page source

def test_show_history(driver):
    driver.get("http://127.0.0.1:5000/history")
    assert "Search History" in driver.title  # Ensure the history page title is correct

    # Optionally, verify if the history list is displayed correctly
    history_items = driver.find_elements(By.TAG_NAME, "li")
    assert len(history_items) > 0  # Ensure there is at least one history item

    # Check the most recent search is listed in history (assuming the first item is the most recent)
    most_recent_item = history_items[0]
    assert "new york" in most_recent_item.text.lower()  # Check if the recent search is listed in history
