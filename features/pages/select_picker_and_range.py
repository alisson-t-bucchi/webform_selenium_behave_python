
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage

class SelectPickerAndRange(BasePage):
    def __init__(self, driver):
        super().__init__(driver)  # Inicializa a classe base
        self.COLOR_INPUT = (By.NAME, "my-colors")
        self.COLOR = "#ff5733"
        self.DATE_INPUT = (By.NAME, "my-date")
        self.DATE = "01-05-2025"
        self.SLIDER = (By.NAME, "my-range")
        self.SLIDER_OFFSET = 30

    def pick_color(self):

        color_input = self.find_element(self.COLOR_INPUT)
        color_input.clear()
        color_input.send_keys(self.COLOR)
        color_input.click()

    def pick_date(self):

        date_input = self.find_element(self.DATE_INPUT)
        date_input.clear()
        date_input.send_keys(self.DATE)
        date_input.click()

    def move_slide(self):

        slider = self.find_element(self.SLIDER)
        actions = ActionChains(self.driver)
        actions.click_and_hold(slider).move_by_offset(self.SLIDER_OFFSET, 0).release().perform()

