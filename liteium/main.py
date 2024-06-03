from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os, pickle
from io import open as io_open
from urllib.parse import urlparse
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

global driver1
driver1 = ''

class ElementWrapper:
    def __init__(self, element):
        self.element = element

class ElementsWrapper:
    def __init__(self, elements):
        self.elements = elements

def driver(driver_path):
    """
    Initialize the WebDriver with the given path.
    
    Parameters:
    driver_path (str): Path to the WebDriver executable.
    
    Returns:
    WebDriver: An instance of the WebDriver.
    """
    try:
        global driver1
        driver1 = webdriver.Chrome(service=Service(driver_path))
        return driver1
    except Exception as e:
        print("An error occurred while initializing driver:", e)

def close():
    """
    Close the WebDriver session.
    """
    try:
        global driver1
        driver1.quit()
    except Exception as e:
        print("An error occurred while closing driver:", e)

def open(url):
    """
    Open the specified URL in the browser.
    
    Parameters:
    url (str): The URL to open.
    """
    try:
        global driver1
        driver1.get(url)
    except Exception as e:
        print("An error occurred while opening URL:", e)

def find_element(by, value, time=0):
    """
    Find a single element by the given locator.
    
    Parameters:
    by (str): The type of locator (e.g., By.ID, By.NAME).
    value (str): The value of the locator.
    time (int, optional): The amount of time to wait for the element to be present. Default is 0.
    
    Returns:
    ElementWrapper: A wrapper around the located element.
    """
    try:
        locator = (by, value)
        wait = WebDriverWait(driver1, time)
        return ElementWrapper(wait.until(EC.presence_of_element_located(locator)))
    except TimeoutException:
        print("Timeout occurred while waiting for element.")
    except NoSuchElementException:
        print("Element not found.")

def find_elements(by, value, time=0):
    """
    Find multiple elements by the given locator.
    
    Parameters:
    by (str): The type of locator (e.g., By.ID, By.NAME).
    value (str): The value of the locator.
    time (int, optional): The amount of time to wait for the elements to be present. Default is 0.
    
    Returns:
    ElementsWrapper: A wrapper around the located elements.
    """
    try:
        locator = (by, value)
        wait = WebDriverWait(driver1, time)
        return ElementsWrapper(wait.until(EC.presence_of_all_elements_located(locator)))
    except Exception as e:
        print("An error occurred while finding elements:", e)

def id(value, time=0):
    """
    Find a single element by ID.
    
    Parameters:
    value (str): The ID of the element.
    time (int, optional): The amount of time to wait for the element to be present. Default is 0.
    
    Returns:
    WebElement: The located element.
    """
    try:
        return find_element(By.ID, value, time).element
    except Exception as e:
        print("An error occurred while finding element by ID:", e)

def name(value, time=0):
    """
    Find a single element by name attribute.
    
    Parameters:
    value (str): The name attribute of the element.
    time (int, optional): The amount of time to wait for the element to be present. Default is 0.
    
    Returns:
    WebElement: The located element.
    """
    try:
        return find_element(By.NAME, value, time).element
    except Exception as e:
        print("An error occurred while finding element by name:", e)

def xpath(value, time=0):
    """
    Find a single element by XPath.
    
    Parameters:
    value (str): The XPath of the element.
    time (int, optional): The amount of time to wait for the element to be present. Default is 0.
    
    Returns:
    WebElement: The located element.
    """
    try:
        return find_element(By.XPATH, value, time).element
    except Exception as e:
        print("An error occurred while finding element by XPath:", e)

def link_text(value, time=0):
    """
    Find a single element by link text.
    
    Parameters:
    value (str): The link text of the element.
    time (int, optional): The amount of time to wait for the element to be present. Default is 0.
    
    Returns:
    WebElement: The located element.
    """
    try:
        return find_element(By.LINK_TEXT, value, time).element
    except Exception as e:
        print("An error occurred while finding element by link text:", e)

def partial_link_text(value, time=0):
    """
    Find a single element by partial link text.
    
    Parameters:
    value (str): The partial link text of the element.
    time (int, optional): The amount of time to wait for the element to be present. Default is 0.
    
    Returns:
    WebElement: The located element.
    """
    try:
        return find_element(By.PARTIAL_LINK_TEXT, value, time).element
    except Exception as e:
        print("An error occurred while finding element by partial link text:", e)

def tag_name(value, time=0):
    """
    Find a single element by tag name.
    
    Parameters:
    value (str): The tag name of the element.
    time (int, optional): The amount of time to wait for the element to be present. Default is 0.
    
    Returns:
    WebElement: The located element.
    """
    try:
        return find_element(By.TAG_NAME, value, time).element
    except Exception as e:
        print("An error occurred while finding element by tag name:", e)

def class_name(value, time=0):
    """
    Find a single element by class name.
    
    Parameters:
    value (str): The class name of the element.
    time (int, optional): The amount of time to wait for the element to be present. Default is 0.
    
    Returns:
    WebElement: The located element.
    """
    try:
        return find_element(By.CLASS_NAME, value, time).element
    except Exception as e:
        print("An error occurred while finding element by class name:", e)

def css_selector(value, time=0):
    """
    Find a single element by CSS selector.
    
    Parameters:
    value (str): The CSS selector of the element.
    time (int, optional): The amount of time to wait for the element to be present. Default is 0.
    
    Returns:
    WebElement: The located element.
    """
    try:
        return find_element(By.CSS_SELECTOR, value, time).element
    except Exception as e:
        print("An error occurred while finding element by CSS selector:", e)

def ids(value, time=0):
    """
    Find multiple elements by ID.
    
    Parameters:
    value (str): The ID of the elements.
    time (int, optional): The amount of time to wait for the elements to be present. Default is 0.
    
    Returns:
    list[WebElement]: The located elements.
    """
    try:
        return find_elements(By.ID, value, time).elements
    except Exception as e:
        print("An error occurred while finding elements by ID:", e)

def names(value, time=0):
    """
    Find multiple elements by name attribute.
    
    Parameters:
    value (str): The name attribute of the elements.
    time (int, optional): The amount of time to wait for the elements to be present. Default is 0.
    
    Returns:
    list[WebElement]: The located elements.
    """
    try:
        return find_elements(By.NAME, value, time).elements
    except Exception as e:
        print("An error occurred while finding elements by name:", e)

def xpaths(value, time=0):
    """
    Find multiple elements by XPath.
    
    Parameters:
    value (str): The XPath of the elements.
    time (int, optional): The amount of time to wait for the elements to be present. Default is 0.
    
    Returns:
    list[WebElement]: The located elements.
    """
    try:
        return find_elements(By.XPATH, value, time).elements
    except Exception as e:
        print("An error occurred while finding elements by XPath:", e)

def link_texts(value, time=0):
    """
    Find multiple elements by link text.
    
    Parameters:
    value (str): The link text of the elements.
    time (int, optional): The amount of time to wait for the elements to be present. Default is 0.
    
    Returns:
    list[WebElement]: The located elements.
    """
    try:
        return find_elements(By.LINK_TEXT, value, time).elements
    except Exception as e:
        print("An error occurred while finding elements by link text:", e)

def partial_link_texts(value, time=0):
    """
    Find multiple elements by partial link text.
    
    Parameters:
    value (str): The partial link text of the elements.
    time (int, optional): The amount of time to wait for the elements to be present. Default is 0.
    
    Returns:
    list[WebElement]: The located elements.
    """
    try:
        return find_elements(By.PARTIAL_LINK_TEXT, value, time).elements
    except Exception as e:
        print("An error occurred while finding elements by partial link text:", e)

def tag_names(value, time=0):
    """
    Find multiple elements by tag name.
    
    Parameters:
    value (str): The tag name of the elements.
    time (int, optional): The amount of time to wait for the elements to be present. Default is 0.
    
    Returns:
    list[WebElement]: The located elements.
    """
    try:
        return find_elements(By.TAG_NAME, value, time).elements
    except Exception as e:
        print("An error occurred while finding elements by tag name:", e)

def class_names(value, time=0):
    """
    Find multiple elements by class name.
    
    Parameters:
    value (str): The class name of the elements.
    time (int, optional): The amount of time to wait for the elements to be present. Default is 0.
    
    Returns:
    list[WebElement]: The located elements.
    """
    try:
        return find_elements(By.CLASS_NAME, value, time).elements
    except Exception as e:
        print("An error occurred while finding elements by class name:", e)

def css_selectors(value, time=0):
    """
    Find multiple elements by CSS selector.
    
    Parameters:
    value (str): The CSS selector of the elements.
    time (int, optional): The amount of time to wait for the elements to be present. Default is 0.
    
    Returns:
    list[WebElement]: The located elements.
    """
    try:
        return find_elements(By.CSS_SELECTOR, value, time).elements
    except Exception as e:
        print("An error occurred while finding elements by CSS selector:", e)

def browser_version():
    """
    Get the version of the browser being used.
    
    Returns:
    str: The version of the browser.
    """
    global driver1
    try:
        return driver1.capabilities['browserVersion']
    except Exception as e:
        print("Exception:", e)
        return ""

def window_position(x, y):
    """
    Set the position of the browser window.
    
    Parameters:
    x (int): The x-coordinate of the window position.
    y (int): The y-coordinate of the window position.
    """
    global driver1
    try:
        driver1.set_window_position(x, y)
    except Exception as e:
        print("Exception:", e)

def window_size(width, height):
    """
    Set the size of the browser window.
    
    Parameters:
    width (int): The width of the window.
    height (int): The height of the window.
    """
    global driver1
    try:
        driver1.set_window_size(width, height)
    except Exception as e:
        print("Exception:", e)

def screenshot(filename=None):
    """
    Take a screenshot and save it to the specified filename.
    
    Parameters:
    filename (str, optional): The name of the file to save the screenshot. Default is "screenshot.png".
    """
    global driver1
    try:
        if filename is None:
            filename = "screenshot.png"
        elif not os.path.isabs(filename):
            filename = os.path.join(os.getcwd(), filename)
        
        driver1.save_screenshot(filename)
        print("Screenshot saved at:", filename)
    except Exception as e:
        print("Exception:", e)

def save_cookies(filename=None):
    """
    Save the browser's cookies to a file.
    
    Parameters:
    filename (str, optional): The name of the file to save the cookies. Default is based on the current URL's hostname.
    """
    try:
        if filename is None:
            current_url = driver1.current_url
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
        
        cookies = driver1.get_cookies()
        with io_open(filename, 'wb') as file:
            pickle.dump(cookies, file)
    except Exception as e:
        print("Exception:", e)

def delete_cookies():
    """
    Delete all cookies in the browser.
    """
    try:
        driver1.delete_all_cookies()
    except Exception as e:
        print("Exception:", e)

def set_cookies(filename):
    """
    Load cookies from a file and set them in the browser.
    
    Parameters:
    filename (str): The name of the file to load the cookies from.
    """
    try:
        with io_open(filename, 'rb') as file:
            cookies = pickle.load(file)

        for cookie in cookies:
            driver1.add_cookie(cookie)
    except Exception as e:
        print("Exception:", e)

def switch_to_alert(action='accept'):
    """
    Switch to an alert and perform an action (accept, cancel, or get text).
    
    Parameters:
    action (str, optional): The action to perform on the alert ('accept', 'cancel', or 'text'). Default is 'accept'.
    
    Returns:
    str: The text of the alert if action is 'text'.
    """
    try:
        alert = driver1.switch_to.alert
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
        print("Exception:", e)

def switch_to_default():
    """
    Switch to the default content (main document).
    """
    try:
        driver1.switch_to.default_content()
    except Exception as e:
        print("Exception:", e)

def switch_to_frame(frame):
    """
    Switch to a specified frame.
    
    Parameters:
    frame: The frame to switch to (can be name, ID, or WebElement).
    """
    try:
        driver1.switch_to.frame(frame)
    except Exception as e:
        print("Exception:", e)

def switch_to_window(index_or_name):
    """
    Switch to a window by index or name.
    
    Parameters:
    index_or_name (int or str): The index or name of the window to switch to.
    """
    try:
        if isinstance(index_or_name, int):
            driver1.switch_to.window(driver1.window_handles[index_or_name])
        else:
            driver1.switch_to.window(index_or_name)
    except Exception as e:
        print("Exception:", e)

def new_window(url="about:blank"):
    """
    Open a new browser window with the specified URL.
    
    Parameters:
    url (str, optional): The URL to open in the new window. Default is "about:blank".
    """
    try:
        driver1.execute_script("window.open(arguments[0], '_blank');", url)
    except Exception as e:
        print("Exception:", e)

def js(script):
    """
    Execute a JavaScript script in the browser.
    
    Parameters:
    script (str): The JavaScript code to execute.
    """
    try:
        driver1.execute_script(script)
    except Exception as e:
        print("Exception:", e)

def refresh():
    """
    Refresh the current page.
    """
    try:
        driver1.refresh()
    except Exception as e:
        print("Exception:", e)

def forward():
    """
    Navigate forward in the browser history.
    """
    try:
        driver1.forward()
    except Exception as e:
        print("Exception:", e)

def back():
    """
    Navigate backward in the browser history.
    """
    try:
        driver1.back()
    except Exception as e:
        print("Exception:", e)

__all__ = ['driver', 'open', 'close', 'id', 'name', 'xpath', 'link_text', 'partial_link_text', 'tag_name', 'class_name', 'css_selector', 
           'ids', 'names', 'xpaths', 'link_texts', 'partial_link_texts', 'tag_names', 'class_names', 'css_selectors', 'browser_version',
           'window_position', 'window_size', 'screenshot', 'save_cookies', 'delete_cookies', 'set_cookies', 'switch_to_alert', 'switch_to_default',
           'switch_to_frame', 'switch_to_window', 'new_window', 'js', 'refresh', 'back', 'forward']
