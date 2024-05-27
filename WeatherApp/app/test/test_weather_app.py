# test_weather_app.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture(scope="module")
def driver():
    # Setup Chrome WebDriver
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_home_page(driver):
    driver.get("http://127.0.0.1:5000/")
    assert "Input Form" in driver.title

def test_weather_search(driver):
    driver.get("http://127.0.0.1:5000/")
    search_box = driver.find_element(By.NAME, "user_input")
    search_box.send_keys("New York")
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)  # Wait for response
    assert "Error" not in driver.page_source

def test_show_history(driver):
    driver.get("http://127.0.0.1:5000/history")
    assert "History" in driver.page_source

if __name__ == "__main__":
    pytest.main()
