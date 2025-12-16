import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

@pytest.fixture
def driver():
    """Setup and teardown for WebDriver"""
    chrome_options = Options()
    chrome_options.binary_location = chrome_path
    chrome_options.add_argument("--headless")  # Run in headless mode for CI
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()
def test_google_title(driver):
    """Test to verify Google homepage title"""
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    print(f"Page title: {driver.title}")

def test_example_domain(driver):
    """Test to verify Example Domain page"""
    driver.get("https://www.example.com")
    assert "Example Domain" in driver.title
    print(f"Page title: {driver.title}")

@pytest.mark.parametrize("url,expected_text", [
    ("https://www.python.org", "Python"),
    ("https://www.github.com", "GitHub")
])
def test_multiple_sites(driver, url, expected_text):
    """Test multiple websites with parameterization"""
    driver.get(url)
    assert expected_text in driver.title

