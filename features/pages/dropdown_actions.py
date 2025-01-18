from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage
from selenium.webdriver.support.ui import Select

class DropdownActions(BasePage):
    def __init__(self, driver):
        super().__init__(driver)  # Inicializa a classe base
        self.SELECT_DROPDOWN = (By.NAME, "my-select")
        self.TEXT_DROPDOWN = "Three"
        self.SELECT_DATALIST = (By.XPATH, "//input[@name='my-datalist']")
        self.TEXT_DATALIST = "San Fransciso"
        self.SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")

    def click_drop(self):

        dropdown_element = self.find_element(self.SELECT_DROPDOWN)
        select = Select(dropdown_element)
        select.select_by_visible_text(self.TEXT_DROPDOWN)

    def click_data(self):

        datalist_input = self.find_element(self.SELECT_DATALIST)
        datalist_input.send_keys(self.TEXT_DATALIST)
