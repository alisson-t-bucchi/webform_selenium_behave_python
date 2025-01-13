from behave import given, when, then
from features.pages.text_input_page import TextInputPage

@given(u'open Web form page')
def acess_page_test(context):
    context.driver.get("https://www.selenium.dev/selenium/web/web-form.html")


@when(u'insert a text "{text_input}" in a Text input area')
def insert_text_input(context, text_input):
    page = TextInputPage(context.driver)
    page.fill_text_input(text_input)


@when(u'insert a pass "{password_input}" in the Password area')
def insert_password(context, password_input):
    page = TextInputPage(context.driver)
    page.fill_password_input(password_input)


@when(u'insert a long text "{textarea_input}" in the Textarea')
def insert_textarea_input(context, textarea_input):
    page = TextInputPage(context.driver)
    page.fill_textarea_input(textarea_input)


@then(u'click on Submit button')
def click_submit_button(context):
    submit = TextInputPage(context.driver)
    submit.click_submit()