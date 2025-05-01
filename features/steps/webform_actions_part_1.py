import time

from behave import given, when, then

from features.pages.base_page import BasePage
from features.pages.text_input_actions import TextInputActions

@given(u'open Web form page for scenario 1')
def acess_page_test(context):
    open_web_form = BasePage(context.driver)
    open_web_form.open_page()

@when(u'insert a text "{text_input}" in a Text input area')
def insert_text_input(context, text_input):
    page = TextInputActions(context.driver)
    page.fill_text_input(text_input)

@when(u'insert a pass "{password_input}" in the Password area')
def insert_password(context, password_input):
    page = TextInputActions(context.driver)
    page.fill_password_input(password_input)

@when(u'insert a long text "{textarea_input}" in the Textarea')
def insert_textarea_input(context, textarea_input):
    page = TextInputActions(context.driver)
    page.fill_textarea_input(textarea_input)

@then(u'click on Submit button for scenario 1')
def click_submit_button(context):
    submit = BasePage(context.driver)
    submit.click_submit_button()