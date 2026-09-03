import pathlib
from behave import given, when, then
from playwright.sync_api import expect

@given('the user opens the Kindergarten Enrollment portal')
def step_impl(context):
    html_path = pathlib.Path(__file__).parent.parent / "fixtures" / "mock_enrollment.html"
    context.page.goto(html_path.as_uri())

@when('the user selects the enrollment year "{year}"')
def step_impl(context, year):
    context.page.select_option("#year", year)

@when('enters the child\'s full name "{child_name}"')
def step_impl(context, child_name):
    context.page.fill("#childName", child_name)

@when('enters parent name "{parent_name}" and email "{email}"')
def step_impl(context, parent_name, email):
    context.page.fill("#parentName", parent_name)
    context.page.fill("#email", email)

@when('clicks the Submit Application button')
def step_impl(context):
    context.page.click("#submitBtn")

@then('the confirmation heading displays "{expected_text}"')
def step_impl(context, expected_text):
    heading = context.page.locator("#confirmationHeader")
    expect(heading).to_be_visible()
    expect(heading).to_have_text(expected_text)

@then('a valid submission timestamp is displayed')
def step_impl(context):
    timestamp = context.page.locator("#timestampPara")
    expect(timestamp).to_be_visible()
    expect(timestamp).to_contain_text("Timestamp:")