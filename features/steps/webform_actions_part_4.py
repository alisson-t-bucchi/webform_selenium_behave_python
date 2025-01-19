import time
from behave import given, when, then
from features.pages.base_page import BasePage
from features.pages.select_picker_and_range import SelectPickerAndRange

time.sleep(5)
@given(u'open Web form page for scenario 4')
def acess_page_test(context):
    open_web_form = BasePage(context.driver)
    open_web_form.open_page()

@when(u'select a color in a color picker')
def select_color_picker(context):
    color = SelectPickerAndRange(context.driver)
    color.pick_color()
    time.sleep(5)

@when(u'select a date in a date picker')
def select_date_picker(context):
    date = SelectPickerAndRange(context.driver)
    date.pick_date()
    time.sleep(5)

@when(u'change the range in example range bar')
def change_range_bar(context):
    range = SelectPickerAndRange(context.driver)
    range.move_slide()

@then(u'click on Submit button for scenario 4')
def click_submit_button(context):
    submit = BasePage(context.driver)
    submit.click_submit_button()