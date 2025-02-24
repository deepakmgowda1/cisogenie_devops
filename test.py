import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://staging.cisogenie.com/en/login")
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("admin-t16@cisogenie.com")
    page.get_by_role("textbox", name="Email").press("Tab")
    page.get_by_role("textbox", name="Password").fill("Password@123")
    page.get_by_role("button", name="Login").click()
    page.get_by_text("Mssp-test9").click()
    page.locator("a").filter(has_text="Policy Management").click()
    page.get_by_role("link", name="Assessments").click()
    page.get_by_role("link", name="Policies").click()
    page.get_by_role("link", name="Task Management").click()
    page.locator("a").filter(has_text="Compliance Management").click()
    page.get_by_role("link", name="Compliance Readiness").click()
    page.get_by_role("link", name="Audit Management").click()
    page.get_by_role("link", name="Documents and Links").click()
    page.locator("a").filter(has_text="Risk Management").click()
    page.get_by_role("link", name="Scans").click()
    page.get_by_role("link", name="Risk Register").click()
    page.get_by_role("link", name="Vendor Management").click()
    page.get_by_role("link", name="Reports").click()
    page.get_by_role("link", name="Users").click()
    page.locator("a").filter(has_text=re.compile(r"^Settings$")).click()
    page.get_by_role("link", name="Account Settings").click()
    page.get_by_role("link", name="Integration").click()
    page.locator(".flex > span > .MuiBadge-badge").click()
    page.get_by_role("button", name="Logout").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
