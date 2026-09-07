import pathlib
from behave import given, when, then
from playwright.sync_api import expect


def _element(context, selector):
    if context.browser_name == "selenium":
        from selenium.webdriver.common.by import By

        return context.page.find_element(By.CSS_SELECTOR, selector)
    return context.page.locator(selector)

@given('the user opens the Kindergarten Enrollment portal')
def step_impl(context):
    html_path = pathlib.Path(__file__).parent.parent / "fixtures" / "mock_enrollment.html"
    if context.browser_name == "selenium":
        context.page.get(html_path.as_uri())
    else:
        context.page.goto(html_path.as_uri())

@when('the user selects the enrollment year "{year}"')
def step_impl(context, year):
    if context.browser_name == "selenium":
        from selenium.webdriver.support.ui import Select

        Select(_element(context, "#year")).select_by_value(year)
    else:
        context.page.select_option("#year", year)

@when('enters the child\'s full name "{child_name}"')
def step_impl(context, child_name):
    if context.browser_name == "selenium":
        field = _element(context, "#childName")
        field.clear()
        field.send_keys(child_name)
    else:
        context.page.fill("#childName", child_name)

@when('enters parent name "{parent_name}" and email "{email}"')
def step_impl(context, parent_name, email):
    if context.browser_name == "selenium":
        for selector, value in (("#parentName", parent_name), ("#email", email)):
            field = _element(context, selector)
            field.clear()
            field.send_keys(value)
    else:
        context.page.fill("#parentName", parent_name)
        context.page.fill("#email", email)

@when('clicks the Submit Application button')
def step_impl(context):
    _element(context, "#submitBtn").click()

@then('the confirmation heading displays "{expected_text}"')
def step_impl(context, expected_text):
    heading = _element(context, "#confirmationHeader")
    if context.browser_name == "selenium":
        assert heading.is_displayed()
        assert heading.text == expected_text
    else:
        expect(heading).to_be_visible()
        expect(heading).to_have_text(expected_text)

@then('a valid submission timestamp is displayed')
def step_impl(context):
    timestamp = _element(context, "#timestampPara")
    if context.browser_name == "selenium":
        assert timestamp.is_displayed()
        assert "Timestamp:" in timestamp.text
    else:
        expect(timestamp).to_be_visible()
        expect(timestamp).to_contain_text("Timestamp:")