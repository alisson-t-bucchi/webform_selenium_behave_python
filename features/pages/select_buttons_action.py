from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage

class SelectButtons(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.CHECKBOX = (By.ID, "my-check-2")
        self.RADIOBUTTON = (By.ID, "my-radio-2")

    def click_checkbox(self):

        self.click_button(self.CHECKBOX)

    def click_radio_button(self):

        self.click_button(self.RADIOBUTTON)