import pathlib
import pytest
from playwright.sync_api import Page, expect

def test_successful_login_displays_user_and_timestamp(page: Page):
    # 1. Obtain absolute file URL for the local HTML test file
    html_path = pathlib.Path(__file__).parent.parent / "utils" / "mock_login.html"
    file_url = html_path.as_uri()

    # 2. Navigate to the login page
    page.goto(file_url)

    # 3. Enter credentials into inputs
    page.fill("#username", "premk")
    page.fill("#password", "password1$")

    # 4. Click the Login button
    page.click("#loginBtn")

    # 5. Assert: Heading contains 'User PREMK logged in'
    welcome_heading = page.locator("#welcomeMessage h1")
    expect(welcome_heading).to_be_visible()
    expect(welcome_heading).to_have_text("User PREMK logged in")

    # 6. Assert: Timestamp paragraph is displayed and contains ISO formatted time
    timestamp_para = page.locator("#welcomeMessage p")
    expect(timestamp_para).to_be_visible()
    expect(timestamp_para).to_contain_text("Timestamp:")