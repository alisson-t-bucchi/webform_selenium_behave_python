from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://www.selenium.dev/selenium/web/web-form.html"
        self.SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")

    def open_page(self):
        return self.driver.get(self.base_url)

    def click_submit_button(self, timeout=10):
        submit_button = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(self.SUBMIT_BUTTON))
        submit_button.click()

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click_button(self, locator, timeout=10):
        return self.find_element(locator, timeout).click()

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
