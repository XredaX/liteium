![liteium banner](assets/images/banner.png)

# liteium: A Lightweight Web Scraping and Automation Library

**liteium** is a user-friendly Python library inspired by Selenium, designed to simplify web scraping and automation tasks, especially for beginners. 

It offers a streamlined interface with intuitive methods, making it easier to interact with web pages and extract data without the need for extensive Selenium knowledge.

## Features ✨

* **Simplified Syntax:**  Focus on clarity and ease of use, allowing you to write concise and readable code. 
* **Lightweight:**  Minimal dependencies, making it a lightweight solution without sacrificing functionality.
* **Common Web Interactions:**  Includes methods for finding elements, interacting with forms, taking screenshots, managing cookies, and more.
* **Exception Handling:**  Provides helpful error messages to guide you through potential issues.

## Installation 🚀

Install liteium using pip:

```bash
pip install liteium
```

## Quick Start 🚗

Here's a basic example of using liteium:

```python
from liteium import *

# Initialize the WebDriver (replace with your chromedriver path)
driver_path = '/path/to/chromedriver'
init_driver(driver_path)

# Open a URL
open_url('https://www.example.com')

# Find an element by ID
element = id('exampleId')
print(element.text)

# Take a screenshot
screenshot('example.png')

# Close the WebDriver
close() 
```

## Key Methods 🗝️

* **`init_driver(driver_path, browser='chrome')`**: Initialize the WebDriver (Chrome or Firefox).
* **`open_url(url)`**: Open a specified URL in the browser.
* **`find_element(by, value, time=10)`**:  Find a single element by various locators (ID, name, XPath, etc.).
* **`find_elements(by, value, time=10)`**: Find multiple elements using the same locator approach.
* **`screenshot(filename=None)`**: Capture a screenshot of the current page.
* **`save_cookies(filename=None)`**: Save the browser's cookies to a file.
* **`delete_cookies()`**: Delete all cookies in the browser.
* **`set_cookies(filename)`**: Load cookies from a file and set them in the browser.
* **`switch_to_alert(action='accept')`**: Interact with browser alerts (accept, cancel, get text).
* **`switch_to_default()`**: Switch back to the main document from a frame or window.
* **`switch_to_frame(frame)`**: Switch to a specific frame within the current page.
* **`switch_to_window(index_or_name)`**: Switch to a particular window (by index or name).
* **`new_window(url='about:blank')`**: Open a new browser window.
* **`js(script)`**: Execute JavaScript code in the browser.
* **`refresh()`**: Refresh the current page.
* **`forward()`**: Navigate forward in the browser's history.
* **`back()`**: Navigate backward in the browser's history.
* **`get_current_url()`**: Get the current URL of the browser.
* **`get_title()`**: Get the title of the current page.

##  Documentation 📚

For a detailed explanation of all available methods and usage examples, please visit the [liteium documentation](https://liteium-doc.vercel.app/).

## Contributing 🤝

Contributions are always welcome! If you have any ideas, feature requests, or bug fixes, please open an issue or submit a pull request on GitHub: [https://github.com/XredaX/liteium](https://github.com/XredaX/liteium).

## Support 📧

If you have any questions or need assistance, feel free to contact me:

* Email: redaelbettioui@gmail.com
* LinkedIn: [https://www.linkedin.com/in/reda-el-bettioui/](https://www.linkedin.com/in/reda-el-bettioui/)

## License 📝

liteium is released under the MIT License. See the LICENSE file for details.

## Star the Repository ⭐

If you find this library helpful, please consider giving it a star on GitHub ⭐ to show your support!