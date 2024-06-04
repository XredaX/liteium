# tests/test_liteium.py

import pytest
from liteium import driver, open, close, class_name

def test_driver_initialization():
    # Initialize the driver
    driver_instance = driver("/usr/local/bin/chromedriver")  # Update with your chromedriver path
    assert driver_instance is not None

def test_open_url():
    driver_instance = driver("/usr/local/bin/chromedriver")  # Update with your chromedriver path
    open("https://google.com")
    assert "Google" in driver_instance.title
    close()

def test_find_element_by_id():
    driver("/usr/local/bin/chromedriver")  # Update with your chromedriver path
    open("https://google.com")
    element = class_name("A8SBwf")  # Replace with an actual element ID on the page
    assert element is not None
    close()

# Add more tests as needed
