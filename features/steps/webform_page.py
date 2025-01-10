import time
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given(u'the browser open Webform page')
def acess_page_test(context):

    context.driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    time.sleep(2)

@when(u'insert a information in the text input field')
def fill_text_input_test(context):

    wait = WebDriverWait(context.driver, 5)
    element = wait.until(EC.visibility_of_element_located((By.NAME, "my-text")))
    element.send_keys("Selenium")

    #context.element = context.driver.find_element(By.NAME, "my-text").send_keys("Selenium")

@then(u'the submit button will be clicked')
def click_submit_button_test(context):

    wait = WebDriverWait(context.driver, 5)
    submit_btn = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn")))
    submit_btn.click()

    #context.element = context.driver.find_element(By.CSS_SELECTOR, ".btn").click()
