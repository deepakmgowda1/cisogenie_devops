from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Set headless=True for silent execution
    page = browser.new_page()

    page.goto("https://www.google.com", timeout=60000)  # Wait up to 60s
    input("Google Opened...")
    page.fill("input[name='q']", "Playwright Automation")
    page.press("input[name='q']", "Enter")

    # Wait for results to appear
    page.wait_for_selector("h3", timeout=5000)

    # Keep the browser open
    input("Press Enter to close the browser...")

    browser.close()