from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver: webdriver.Edge  # Updated type annotation for Edge

def before_all(context):
    global driver
    # Use EdgeDriverManager to automatically install and manage the correct EdgeDriver
    service = Service(EdgeChromiumDriverManager().install())
    context.driver = webdriver.Edge(service=service)
    context.driver.maximize_window()

def after_step(context, step):
    # Optional: Clear cookies and refresh after each step (if necessary)
    context.driver.delete_all_cookies()
    context.driver.refresh()

def after_all(context):
    # Properly quit the driver after all tests
    if hasattr(context, 'driver'):
        context.driver.quit()

