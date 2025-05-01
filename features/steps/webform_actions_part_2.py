import time
from behave import given, when, then

from features.pages.base_page import BasePage
from features.pages.dropdown_actions import DropdownActions

@given(u'open Web form page for scenario 2')
def acess_page_test(context):
    open_web_form = BasePage(context.driver)
    open_web_form.open_page()

@when(u'select option "Two"')
def click_two(context):
    select_drop = DropdownActions(context.driver)
    select_drop.click_drop()

@when(u'select option  "Los Angeles"')
def selecting_los_angeles(context):
    select_data = DropdownActions(context.driver)
    select_data.click_data()

@then(u'click on Submit button for scenario 2')
def click_submit_button(context):
    submit = BasePage(context.driver)
    submit.click_submit_button()