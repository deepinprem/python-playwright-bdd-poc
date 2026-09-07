import os


def _use_selenium():
    return os.getenv("BDD_BROWSER", "playwright").lower() == "selenium"

def _create_selenium_driver():
    from selenium import webdriver

    options = webdriver.ChromeOptions()
    if os.getenv("CI") or os.getenv("BDD_HEADLESS", "true").lower() == "true":
        options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=options)

def before_all(context):
    context.browser_name = os.getenv("BDD_BROWSER", "playwright").lower()
    if _use_selenium():
        return

    from playwright.sync_api import sync_playwright

    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False, slow_mo=1000)

def before_scenario(context, scenario):
    if _use_selenium():
        context.page = _create_selenium_driver()
    else:
        context.page = context.browser.new_page()

def after_scenario(context, scenario):
    if _use_selenium():
        context.page.quit()
    else:
        context.page.close()

def after_all(context):
    if not _use_selenium() and hasattr(context, "browser"):
        context.browser.close()
        context.playwright.stop()