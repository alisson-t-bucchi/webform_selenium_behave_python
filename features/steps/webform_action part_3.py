import time

from behave import given, when, then

from features.pages.base_page import BasePage
from features.pages.file_input_action import FileInput
from features.pages.select_buttons_action import SelectButtons

time.sleep(5)
@given(u'open Web form page for scenario 3')
def acess_page_test(context):
    open_web_form = BasePage(context.driver)
    open_web_form.open_page()

@when(u'choose one file and upload')
def choose_file_and_upload(context):
    upload_file = FileInput(context.driver)
    upload_file.file_input()

@when(u'click on Default checkbox')
def click_checkbox(context):
    click_button_1 = SelectButtons(context.driver)
    click_button_1.click_checkbox()

@when(u'click on Default radio')
def click_radio_button(context):
    click_button_2 = SelectButtons(context.driver)
    click_button_2.click_radio_button()

@then(u'click on Submit button for scenario 3')
def click_submit_button(context):
    submit = BasePage(context.driver)
    submit.click_submit_button()