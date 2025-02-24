from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Change to True for headless mode
        context = browser.new_context()
        page = context.new_page()

        # Open login page
        page.goto("https://staging.cisogenie.com/en/login")

        # Enter email
        page.fill("input[name='email']", "admin-t13@cisogenie.com")

        # Enter password
        page.fill("input[id='login-password']", "Password@123")

        # Click login button
        page.click("button[type='submit']")

        # Wait for login success (Dashboard check)
        if page.wait_for_selector("h1:has-text('Dashboard')"):
            print("✅ Login successful!")
        else:
            print("❌ Login failed!")

        browser.close()

if __name__ == "__main__":
    run()
