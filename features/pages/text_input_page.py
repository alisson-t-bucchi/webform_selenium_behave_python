from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage

class TextInputPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.TEXT_INPUT = (By.ID, "my-text-id")
        self.PASSWORD_INPUT = (By.NAME, "my-password")
        self.TEXTAREA_INPUT = (By.NAME, "my-textarea")
        self.SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")

    def fill_text_input(self, text):
        element = self.wait_for_element(self.TEXT_INPUT)
        element.clear()
        element.send_keys(text)

    def fill_password_input(self, password):
        element = self.wait_for_element(self.PASSWORD_INPUT)
        element.clear()
        element.send_keys(password)

    def fill_textarea_input(self, text):
        element = self.wait_for_element(self.TEXTAREA_INPUT)
        element.clear()
        element.send_keys(text)

    def click_submit(self):
        self.click_button(self.SUBMIT_BUTTON)
