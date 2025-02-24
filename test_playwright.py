from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Set to True to run headless
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.fill("input[name='q']", "Playwright Automation")
    page.press("input[name='q']", "Enter")
    page.wait_for_timeout(3000)
    browser.close()
