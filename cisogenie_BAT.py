
import pytest
import re
import time
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def setup():
    """Setup Playwright browser and page context"""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(viewport={"width": 1020, "height": 1020})
        page = context.new_page()
        yield page
        context.close()
        browser.close()

def test_bat(setup):
    """Test Login"""
    page = setup
    acc= "Mssp-test10"
    page.goto("https://staging.cisogenie.com/en/login")
    try:
        print("Login started")
        page.get_by_role("textbox", name="Email").click()
        page.get_by_role("textbox", name="Email").fill("admin-t4@cisogenie.com")
        page.get_by_role("textbox", name="Password").click()
        page.get_by_role("textbox", name="Password").fill("Password@123")
        page.get_by_role("button", name="Login").click()
        print("Login successful")
        page.screenshot(path="D:/College/Cloudurity/cisogenie-tests/screenshots/login-success-MSSP-task.png")
    except:
        print("Login failed")
    try:
        print("Trying to create Account ")
        page.get_by_role("button", name="Add New Account").click()
        page.get_by_role("textbox", name="Sub Account Name*").click()
        page.get_by_role("textbox", name="Sub Account Name*").fill(acc)
        page.get_by_role("textbox", name="Industry*").click()
        page.get_by_role("textbox", name="Industry*").fill("Automobile")
        page.locator("input[name=\"features\\.compliance\"]").check()
        page.locator("input[name=\"features\\.reports\\.reports\"]").check()
        page.get_by_role("button", name="Create").click()
        print("Account creation successful")
        page.screenshot(path="D:/College/Cloudurity/cisogenie-tests/screenshots/account-creation-MSSP-task.png")
    except:
        print("Account creation failed")
    
    try:
        print("Selecting Account ")
        page.get_by_role("combobox", name="10").click()
        page.get_by_role("option", name="50").click()
        page.get_by_text(acc).click()
        time.sleep(5)
        print("Account selection successful")
        page.screenshot(path="D:/College/Cloudurity/cisogenie-tests/screenshots/account-selection-MSSP-task.png")
    except:
        print("Account selection failed")
    try:
        print("Navigation to assessment started")
        page.get_by_role("banner").locator("i").first.click()
        page.locator("a").filter(has_text="Policy Management").click()
        page.get_by_role("link", name="Assessments").click()
        print("Navigation to assessment successful")
        page.screenshot(path="D:/College/Cloudurity/cisogenie-tests/screenshots/assessment-navigation-MSSP-task.png")
    except:
        print("Navigation to assessment failed")
    try:
        print("Questionare 1 (Profiling) started")
    
        page.get_by_role("button", name="Start").first.click()
        page.get_by_role("button", name="More than").click()
        page.get_by_role("button", name="IT Department supported by").click()
        page.locator("div").filter(has_text=re.compile(r"^3\. Can your company's resources be accessed remotely\?NoYes$")).get_by_role("button").first.click()
        page.get_by_role("button", name="On Premises & Cloud").click()
        page.locator("div").filter(has_text=re.compile(r"^5\. Does your company use SaaS products\?NoYes$")).get_by_role("button").first.click()
        page.locator("div").filter(has_text=re.compile(r"^6\. Do you have a centralized directory service for user authentication\?NoYes$")).get_by_role("button").first.click()
        page.locator("div").filter(has_text=re.compile(r"^8\. Does your company process credit card payments\?NoYes$")).get_by_role("button").first.click()
        page.locator("div").filter(has_text=re.compile(r"^7\. Does your company handle or store PII\?NoYes$")).get_by_role("button").first.click()
        page.locator("div").filter(has_text=re.compile(r"^9\. Does your company use Generative AI\?NoYes$")).get_by_role("button").first.click()
        page.locator("div:nth-child(11) > .flex > button").first.click()
        page.locator("div:nth-child(12) > .flex > button").first.click()
        page.locator("div").filter(has_text=re.compile(r"^10\. Does your company create software\?NoYes$")).get_by_role("button").first.click()
        page.get_by_role("button", name="Box", exact=True).click()
        page.get_by_role("button", name="Submit", exact=True).click()
    except:
        print("Questionare 1 failed")
    try:
        print("Questionare 2 (Compliance) started")
        time.sleep(5)
        page.get_by_role("button", name="Start").click()
        page.get_by_role("button", name="ISO 27001-2022").click()
        page.get_by_role("button", name="Submit", exact=True).click()
        print("Questionare 2 successful")
        page.screenshot(path="D:/College/Cloudurity/cisogenie-tests/screenshots/questionare2-MSSP-task.png")
    except:
        print("Questionare 2 failed")
    time.sleep(5)
    try:
        print("Env policies started")

        page.locator("a > .MuiButtonBase-root").first.click()
        page.locator("div").filter(has_text=re.compile(r"^1\. Are risk assessments conducted regularly\?Don't knowNoYes$")).get_by_role("button").first.click()
        page.locator("div:nth-child(2) > .flex > button").first.click()
        page.locator("div").filter(has_text=re.compile(r"^3\. Are flood detection and response systems in place\?Don't knowNoYes$")).get_by_role("button").first.click()
        page.locator("div").filter(has_text=re.compile(r"^4\. Are power surge protection measures in place\?Don't knowNoYes$")).get_by_role("button").first.click()
        page.locator("div").filter(has_text=re.compile(r"^5\. Are environmental conditions monitored in critical areas\?Don't knowNoYes$")).get_by_role("button").first.click()
        page.locator("div").filter(has_text=re.compile(r"^7\. Is the environmental security policy reviewed regularly\?Don't knowNoYes$")).get_by_role("button").first.click()
        page.locator("div:nth-child(6) > .flex > button").first.click()
        page.locator("div:nth-child(8) > .flex > button").first.click()
        page.locator("div:nth-child(9) > .flex > button").first.click()
        page.get_by_role("button", name="Submit", exact=True).click()
        print("Env policies complered successfully")
        page.screenshot(path="D:/College/Cloudurity/cisogenie-tests/screenshots/risk-assessment-MSSP-task.png")
    except:
        print("Env Policies failed")    
    time.sleep(5)
    
    try:
        print("Policy into task management started")
        page.get_by_role("banner").locator("i").first.click()
        page.locator("a").filter(has_text="Policy Management").click()
        page.get_by_role("link", name="Policies").click()
        time.sleep(2)
        page.get_by_role("button", name="View Policy").click()
        page.get_by_role("region", name="1. Flood Detection and").get_by_role("button").click()
        page.get_by_role("checkbox", name="Submit Offline Evidence").check()
        page.get_by_text("TODO").click()
        page.get_by_role("option", name="Done").click()
        page.locator("#select-plan").click()
        page.get_by_role("option", name="Medium term").click()
        page.screenshot(path="D:/College/Cloudurity/cisogenie-tests/screenshots/policy-into-task-management-MSSP-task.png")
    except:
        print("Policy into task management failed")    
    time.sleep(5)
    try:
        print("Entering task management")
        page.get_by_role("banner").locator("i").first.click()
        page.get_by_role("link", name="Task Management").click()
        time.sleep(3)
        print("Entered task management page successfully")
        page.screenshot(path="D:/College/Cloudurity/cisogenie-tests/screenshots/task-management-MSSP-task.png")
    except:
        print("Entering task management failed")
    try:
        print("Entering task 1 through task listing")
        page.get_by_role("link", name="Conduct Risk Assessment").click()
        page.get_by_role("checkbox", name="Submit Offline Evidence").check()
        page.get_by_text("TODO").click()
        page.get_by_role("option", name="Done").click()
        page.screenshot(path="D:/College/Cloudurity/cisogenie-tests/screenshots/task1-MSSP-task.png")
    except:
        print("could not enter task 1 through task listing")
    time.sleep(5)
    try:
        print("entering compliance management")
        page.get_by_role("banner").locator("i").first.click()
        page.locator("a").filter(has_text="Compliance Management").click()
        page.get_by_role("link", name="Compliance Readiness").click()
        print("entered compliance management")
        page.screenshot(path="D:/College/Cloudurity/cisogenie-tests/screenshots/compliance-management-MSSP-task.png")
    except:
        print("could not enter compliance management")
    time.sleep(5)
    try:
        print("compliance readiness started(changing the 1st control)")
        page.get_by_text("Protecting against physical").click()
        page.get_by_role("combobox", name="Not Implemented").click()
        page.get_by_role("option", name="Implemented", exact=True).click()
        page.get_by_text("Protecting against physical").click()
        page.get_by_role("combobox", name="Not Ready for Audit").click()
        page.get_by_role("option", name="Ready For Audit", exact=True).click()

        page.screenshot(path="D:/College/Cloudurity/cisogenie-tests/screenshots/compliance-readiness-MSSP-task.png")
    except:
        print("could not complete compliance readiness")
    time.sleep(5)
    try:
        print("navigating to audit management")
        page.get_by_role("banner").locator("i").first.click()
        page.get_by_role("link", name="Audit Management").click()
        print("navigated to audit management")
        page.screenshot(path="D:/College/Cloudurity/cisogenie-tests/screenshots/audit-management-MSSP-task.png")
    except:
        print("could not enter audit management")
    time.sleep(3)
    # page.get_by_role("button", name="Create Audit").click()
    # page.get_by_role("textbox", name="Audit Name").click()
    # page.get_by_role("textbox", name="Audit Name").fill("audit 1")
    # page.locator("#mui-component-select-compliance_id").click()
    # page.get_by_role("option", name="ISO 27001-").click()
    # page.get_by_role("combobox", name="Select Option").click()
    # page.get_by_role("option", name="Trial").click()
    # page.locator("div").filter(has_text=re.compile(r"^Audit Start Date$")).get_by_placeholder("Click to select a date").click()
    # page.locator("div").filter(has_text=re.compile(r"^Audit Start Date$")).get_by_placeholder("Click to select a date").fill("12/01/2025")
    # page.locator("div").filter(has_text=re.compile(r"^Audit ETA$")).get_by_placeholder("Click to select a date").click()
    # page.locator("div").filter(has_text=re.compile(r"^Audit ETA$")).get_by_placeholder("Click to select a date").fill("12/02/2025")
    # page.get_by_role("textbox", name="Audit Firm").click()
    # page.get_by_role("textbox", name="Audit Firm").fill("sfs")
    # page.get_by_role("button", name="Submit").click()
    # time.sleep(5)
    # # page.get_by_role("button", name="Open Audit").click()
    # # page.get_by_text("Supporting Utilities").click()
    # # page.get_by_role("banner").locator("i").first.click()
    # # page.locator("a").filter(has_text="Risk Management").click()
    # # page.get_by_role("link", name="Risk Register").click()

    # try:
    #     print("creating audit")
    #     page.get_by_role("button", name="Create Audit").click()
    #     page.get_by_role("textbox", name="Audit Name").click()
    #     page.get_by_role("textbox", name="Audit Name").fill("audir")
    #     page.locator("#mui-component-select-compliance_id").click()
    #     page.get_by_role("option", name="ISO 27001-").click()
    #     page.get_by_role("combobox", name="Select Option").click()
    #     page.get_by_role("option", name="Trial").click()
    #     page.locator("div").filter(has_text=re.compile(r"^Audit Start Date$")).get_by_placeholder("Click to select a date").click()
    #     page.locator("div").filter(has_text=re.compile(r"^Audit Start Date$")).get_by_placeholder("Click to select a date").fill("12/10/2024")
    #     page.locator("div").filter(has_text=re.compile(r"^Audit ETA$")).get_by_placeholder("Click to select a date").click()
    #     page.locator("div").filter(has_text=re.compile(r"^Audit ETA$")).get_by_placeholder("Click to select a date").fill("12/12/2024")
    #     page.get_by_role("option", name="Select option").click()
    #     page.get_by_role("textbox", name="Audit Firm").fill("fdsff")
    #     page.get_by_role("textbox", name="Notes").click()
    #     page.get_by_role("textbox", name="Notes").fill("sfsf")
    #     page.get_by_role("button", name="Submit").click()
    #     print("audit created")
    #     page.screenshot(path="D:/College/Cloudurity/cisogenie-tests/screenshots/audit-creation-MSSP-task.png")
    # except:
    #     print("could not create audit")
    
    # ---------------------