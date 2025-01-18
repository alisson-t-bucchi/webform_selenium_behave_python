from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage

class FileInput(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.FILE_PATH = "C:/Users/aliss/PycharmProjects/webform_selenium_behave_python/GitCheatSheet.pdf"
        self.FILE_INPUT = (By.NAME, "my-file")

    def file_input(self,):
        file_input = self.find_element(self.FILE_INPUT)
        file_input.send_keys(self.FILE_PATH)