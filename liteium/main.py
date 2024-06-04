from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os, pickle
from io import open as io_open
from urllib.parse import urlparse
from selenium.common.exceptions import NoAlertPresentException, TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Constants for common locators
ID = By.ID
NAME = By.NAME
XPATH = By.XPATH
LINK_TEXT = By.LINK_TEXT
PARTIAL_LINK_TEXT = By.PARTIAL_LINK_TEXT
TAG_NAME = By.TAG_NAME
CLASS_NAME = By.CLASS_NAME
CSS_SELECTOR = By.CSS_SELECTOR

# Global driver variable
global driver
driver = None

class ElementWrapper:
    """Wrapper class for interacting with a single element"""
    def __init__(self, element):
        self.element = element

    def __getattr__(self, name):
        """Proxies attribute access to the underlying WebElement"""
        return getattr(self.element, name)

class ElementsWrapper:
    """Wrapper class for interacting with multiple elements"""
    def __init__(self, elements):
        self.elements = elements

    def __len__(self):
        """Returns the number of elements in the list"""
        return len(self.elements)

    def __getitem__(self, index):
        """Accesses an element by its index"""
        return self.elements[index]

    def __iter__(self):
        """Iterates through the list of elements"""
        return iter(self.elements)

    def get_attribute(self, attribute):
        """Gets the specified attribute from all elements"""
        return [element.get_attribute(attribute) for element in self.elements]

    def click(self):
        """Clicks on all elements in the list"""
        for element in self.elements:
            try:
                element.click()
            except ElementClickInterceptedException:
                # Attempt to click again after a short delay
                # This can help with elements that are hidden or partially obscured
                WebDriverWait(driver, 1).until(EC.element_to_be_clickable(element))
                element.click()

    def send_keys(self, text):
        """Sends keys to all elements in the list"""
        for element in self.elements:
            element.send_keys(text)

def init_driver(driver_path, browser="chrome"):
    """
    Initializes the WebDriver.

    Args:
        driver_path (str): Path to the WebDriver executable.
        browser (str, optional): The browser to use (e.g., "chrome", "firefox"). Defaults to "chrome".

    Returns:
        WebDriver: An instance of the WebDriver.
    """
    global driver
    try:
        if browser.lower() == "chrome":
            driver = webdriver.Chrome(service=Service(driver_path))
        elif browser.lower() == "firefox":
            driver = webdriver.Firefox(executable_path=driver_path)
        else:
            raise ValueError(f"Unsupported browser: {browser}")
        return driver
    except Exception as e:
        print(f"Error initializing driver: {e}")
        return None

def close():
    """Closes the WebDriver session."""
    global driver
    try:
        if driver:
            driver.quit()
            driver = None
    except Exception as e:
        print(f"Error closing driver: {e}")

def open_url(url):
    """
    Opens the specified URL in the browser.

    Args:
        url (str): The URL to open.
    """
    global driver
    try:
        if driver:
            driver.get(url)
        else:
            print("Driver is not initialized. Please call 'init_driver' function first.")
    except Exception as e:
        print(f"Error opening URL: {e}")

def find_element(by, value, time=10):
    """
    Finds a single element by the given locator.

    Args:
        by (By): The type of locator (e.g., By.ID, By.NAME).
        value (str): The locator value.
        time (int, optional): The maximum time to wait for the element. Defaults to 10.

    Returns:
        ElementWrapper: A wrapped WebElement.
    """
    global driver
    try:
        locator = (by, value)
        wait = WebDriverWait(driver, time)
        return ElementWrapper(wait.until(EC.presence_of_element_located(locator)))
    except TimeoutException:
        print(f"Timeout occurred while waiting for element: {by}='{value}'")
    except NoSuchElementException:
        print(f"Element not found: {by}='{value}'")

def find_elements(by, value, time=10):
    """
    Finds multiple elements by the given locator.

    Args:
        by (By): The type of locator (e.g., By.ID, By.NAME).
        value (str): The locator value.
        time (int, optional): The maximum time to wait for the elements. Defaults to 10.

    Returns:
        ElementsWrapper: A wrapped list of WebElements.
    """
    global driver
    try:
        locator = (by, value)
        wait = WebDriverWait(driver, time)
        return ElementsWrapper(wait.until(EC.presence_of_all_elements_located(locator)))
    except TimeoutException:
        print(f"Timeout occurred while waiting for elements: {by}='{value}'")
    except NoSuchElementException:
        print(f"Elements not found: {by}='{value}'")

# Simplified functions for finding elements by specific locators
def id(value, time=10):
    """Finds a single element by ID."""
    return find_element(ID, value, time)

def name(value, time=10):
    """Finds a single element by name attribute."""
    return find_element(NAME, value, time)

def xpath(value, time=10):
    """Finds a single element by XPath."""
    return find_element(XPATH, value, time)

def link_text(value, time=10):
    """Finds a single element by link text."""
    return find_element(LINK_TEXT, value, time)

def partial_link_text(value, time=10):
    """Finds a single element by partial link text."""
    return find_element(PARTIAL_LINK_TEXT, value, time)

def tag_name(value, time=10):
    """Finds a single element by tag name."""
    return find_element(TAG_NAME, value, time)

def class_name(value, time=10):
    """Finds a single element by class name."""
    return find_element(CLASS_NAME, value, time)

def css_selector(value, time=10):
    """Finds a single element by CSS selector."""
    return find_element(CSS_SELECTOR, value, time)

# Simplified functions for finding multiple elements by specific locators
def ids(value, time=10):
    """Finds multiple elements by ID."""
    return find_elements(ID, value, time)

def names(value, time=10):
    """Finds multiple elements by name attribute."""
    return find_elements(NAME, value, time)

def xpaths(value, time=10):
    """Finds multiple elements by XPath."""
    return find_elements(XPATH, value, time)

def link_texts(value, time=10):
    """Finds multiple elements by link text."""
    return find_elements(LINK_TEXT, value, time)

def partial_link_texts(value, time=10):
    """Finds multiple elements by partial link text."""
    return find_elements(PARTIAL_LINK_TEXT, value, time)

def tag_names(value, time=10):
    """Finds multiple elements by tag name."""
    return find_elements(TAG_NAME, value, time)

def class_names(value, time=10):
    """Finds multiple elements by class name."""
    return find_elements(CLASS_NAME, value, time)

def css_selectors(value, time=10):
    """Finds multiple elements by CSS selector."""
    return find_elements(CSS_SELECTOR, value, time)

def browser_version():
    """
    Gets the version of the browser being used.

    Returns:
        str: The browser version.
    """
    global driver
    try:
        return driver.capabilities['browserVersion']
    except Exception as e:
        print(f"Exception getting browser version: {e}")
        return ""

def window_position(x, y):
    """
    Sets the position of the browser window.

    Args:
        x (int): The x-coordinate of the window.
        y (int): The y-coordinate of the window.
    """
    global driver
    try:
        driver.set_window_position(x, y)
    except Exception as e:
        print(f"Exception setting window position: {e}")

def window_size(width, height):
    """
    Sets the size of the browser window.

    Args:
        width (int): The width of the window.
        height (int): The height of the window.
    """
    global driver
    try:
        driver.set_window_size(width, height)
    except Exception as e:
        print(f"Exception setting window size: {e}")

def screenshot(filename=None):
    """
    Takes a screenshot and saves it to the specified filename.

    Args:
        filename (str, optional): The filename for the screenshot. Defaults to "screenshot.png".
    """
    global driver
    try:
        if filename is None:
            filename = "screenshot.png"
        elif not os.path.isabs(filename):
            filename = os.path.join(os.getcwd(), filename)

        driver.save_screenshot(filename)
        print(f"Screenshot saved at: {filename}")
    except Exception as e:
        print(f"Exception taking screenshot: {e}")

def save_cookies(filename=None):
    """
    Saves the browser's cookies to a file.

    Args:
        filename (str, optional): The filename for saving cookies. Defaults to None.
    """
    global driver
    try:
        if filename is None:
            current_url = driver.current_url
            parsed_url = urlparse(current_url)
            hostname = parsed_url.hostname
            if hostname:
                if hostname.startswith("www."):
                    hostname = hostname[4:]
                if "." in hostname:
                    hostname = hostname.split(".")[0]
                filename = hostname + ".pkl"
            else:
                filename = "cookies.pkl"

        if not os.path.isabs(filename):
            filename = os.path.join(os.getcwd(), filename)

        cookies = driver.get_cookies()
        with io_open(filename, 'wb') as file:
            pickle.dump(cookies, file)
    except Exception as e:
        print(f"Exception saving cookies: {e}")

def delete_cookies():
    """Deletes all cookies in the browser."""
    global driver
    try:
        driver.delete_all_cookies()
    except Exception as e:
        print(f"Exception deleting cookies: {e}")

def set_cookies(filename):
    """
    Loads cookies from a file and sets them in the browser.

    Args:
        filename (str): The filename from which to load cookies.
    """
    global driver
    try:
        with io_open(filename, 'rb') as file:
            cookies = pickle.load(file)

        for cookie in cookies:
            driver.add_cookie(cookie)
    except Exception as e:
        print(f"Exception setting cookies: {e}")

def switch_to_alert(action='accept'):
    """
    Switches to an alert and performs an action (accept, cancel, or get text).

    Args:
        action (str, optional): The action to perform on the alert ('accept', 'cancel', or 'text'). Defaults to 'accept'.

    Returns:
        str: The text of the alert if action is 'text'.
    """
    global driver
    try:
        alert = driver.switch_to.alert
        if action == 'accept':
            alert.accept()
        elif action == 'cancel':
            alert.dismiss()
        elif action == 'text':
            return alert.text
        else:
            print("Invalid action specified.")
    except NoAlertPresentException:
        print("No alert present")
    except Exception as e:
        print(f"Exception switching to alert: {e}")

def switch_to_default():
    """Switches to the default content (main document)."""
    global driver
    try:
        driver.switch_to.default_content()
    except Exception as e:
        print(f"Exception switching to default content: {e}")

def switch_to_frame(frame):
    """
    Switches to a specified frame.

    Args:
        frame (str, int, or WebElement): The frame to switch to (can be name, ID, index, or WebElement).
    """
    global driver
    try:
        driver.switch_to.frame(frame)
    except Exception as e:
        print(f"Exception switching to frame: {e}")

def switch_to_window(index_or_name):
    """
    Switches to a window by index or name.

    Args:
        index_or_name (int or str): The index or name of the window to switch to.
    """
    global driver
    try:
        if isinstance(index_or_name, int):
            driver.switch_to.window(driver.window_handles[index_or_name])
        else:
            driver.switch_to.window(index_or_name)
    except Exception as e:
        print(f"Exception switching to window: {e}")

def new_window(url="about:blank"):
    """
    Opens a new browser window with the specified URL.

    Args:
        url (str, optional): The URL to open in the new window. Defaults to "about:blank".
    """
    global driver
    try:
        driver.execute_script("window.open(arguments[0], '_blank');", url)
    except Exception as e:
        print(f"Exception opening new window: {e}")

def js(script):
    """
    Executes a JavaScript script in the browser.

    Args:
        script (str): The JavaScript code to execute.
    """
    global driver
    try:
        driver.execute_script(script)
    except Exception as e:
        print(f"Exception executing JavaScript: {e}")

def refresh():
    """Refreshes the current page."""
    global driver
    try:
        driver.refresh()
    except Exception as e:
        print(f"Exception refreshing page: {e}")

def forward():
    """Navigates forward in the browser history."""
    global driver
    try:
        driver.forward()
    except Exception as e:
        print(f"Exception navigating forward: {e}")

def back():
    """Navigates backward in the browser history."""
    global driver
    try:
        driver.back()
    except Exception as e:
        print(f"Exception navigating backward: {e}")

def get_current_url():
    """
    Returns the current URL of the browser.

    Returns:
        str: The current URL.
    """
    global driver
    try:
        return driver.current_url
    except Exception as e:
        print(f"Exception getting current URL: {e}")
        return ""

def get_title():
    """
    Returns the title of the current page.

    Returns:
        str: The current page title.
    """
    global driver
    try:
        return driver.title
    except Exception as e:
        print(f"Exception getting page title: {e}")
        return ""

def wait_for_element_to_be_clickable(element, time=10):
    """
    Waits for the specified element to become clickable.

    Args:
        element (WebElement): The element to wait for.
        time (int, optional): The maximum time to wait for the element. Defaults to 10.
    """
    global driver
    try:
        wait = WebDriverWait(driver, time)
        wait.until(EC.element_to_be_clickable(element))
    except TimeoutException:
        print(f"Timeout occurred while waiting for element to be clickable.")
    except Exception as e:
        print(f"Exception waiting for element to be clickable: {e}")

def wait_for_element_to_be_visible(element, time=10):
    """
    Waits for the specified element to become visible.

    Args:
        element (WebElement): The element to wait for.
        time (int, optional): The maximum time to wait for the element. Defaults to 10.
    """
    global driver
    try:
        wait = WebDriverWait(driver, time)
        wait.until(EC.visibility_of(element))
    except TimeoutException:
        print(f"Timeout occurred while waiting for element to be visible.")
    except Exception as e:
        print(f"Exception waiting for element to be visible: {e}")

def scroll_to_element(element):
    """
    Scrolls the page to the specified element.

    Args:
        element (WebElement): The element to scroll to.
    """
    global driver
    try:
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
    except Exception as e:
        print(f"Exception scrolling to element: {e}")

def hover_over_element(element):
    """
    Hovers the mouse over the specified element.

    Args:
        element (WebElement): The element to hover over.
    """
    global driver
    try:
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
    except Exception as e:
        print(f"Exception hovering over element: {e}")

def clear_input_field(element):
    """
    Clears the text content of an input field.

    Args:
        element (WebElement): The input field to clear.
    """
    global driver
    try:
        element.clear()
    except Exception as e:
        print(f"Exception clearing input field: {e}")

def enter_text_in_input_field(element, text):
    """
    Enters text into an input field.

    Args:
        element (WebElement): The input field to enter text into.
        text (str): The text to enter.
    """
    global driver
    try:
        element.send_keys(text)
    except Exception as e:
        print(f"Exception entering text in input field: {e}")

def press_enter_key(element):
    """
    Simulates pressing the Enter key in an input field.

    Args:
        element (WebElement): The input field to press Enter in.
    """
    global driver
    try:
        element.send_keys(Keys.RETURN)
    except Exception as e:
        print(f"Exception pressing Enter key: {e}")

def submit_form(element):
    """
    Submits a form.

    Args:
        element (WebElement): The form element to submit.
    """
    global driver
    try:
        element.submit()
    except Exception as e:
        print(f"Exception submitting form: {e}")

__all__ = ['init_driver', 'open_url', 'close', 'id', 'name', 'xpath', 'link_text', 'partial_link_text', 'tag_name', 'class_name', 'css_selector',
           'ids', 'names', 'xpaths', 'link_texts', 'partial_link_texts', 'tag_names', 'class_names', 'css_selectors',
           'browser_version', 'window_position', 'window_size', 'screenshot', 'save_cookies', 'delete_cookies', 'set_cookies',
           'switch_to_alert', 'switch_to_default', 'switch_to_frame', 'switch_to_window', 'new_window', 'js', 'refresh',
           'back', 'forward', 'get_current_url', 'get_title', 'wait_for_element_to_be_clickable', 'wait_for_element_to_be_visible',
           'scroll_to_element', 'hover_over_element', 'clear_input_field', 'enter_text_in_input_field', 'press_enter_key',
           'submit_form']