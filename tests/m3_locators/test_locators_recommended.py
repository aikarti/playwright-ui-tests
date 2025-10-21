from playwright.sync_api import Page, expect, BrowserType
from tests.utils.constants import BASE_URL
import os


# to slow things down

def test_headless_and_slow_mo(browser_type: BrowserType):
    headless = os.getenv("HEADLESS", "true").lower() == "true"
    slow_mo = int(os.getenv("SLOW_MO", "0"))
    browser = browser_type.launch(headless=headless, slow_mo=slow_mo)
    page = browser.new_page()

#def test_headless_and_slow_mo(browser_type: BrowserType):    
#    browser = browser_type.launch(headless=True, slow_mo=2000)
#    page = browser.new_page()


def test_recommended_locators(page: Page):
    page.goto(BASE_URL)
    expect(page).to_have_title("Credit Association")
    page.get_by_label("First name").fill("Karthick")
    page.get_by_label("Last name").fill("Murugan")
    page.get_by_label("Email").fill("ab@example.com")

    page.get_by_role("button", name="Register", exact=True).click()

def test_warningmessage_on_fields(page: Page):
    page.goto(BASE_URL)
    page.get_by_role("button", name="Register", exact=True).click()
    expect(page.get_by_text("Valid first name is required")).to_be_visible(), "First name warning message is not visible"
    expect(page.get_by_text("Valid last name is required")).to_be_visible(), "Last name warning message is not visible"
    expect(page.get_by_text("Please enter a valid email address")).to_be_visible(), "Email warning message is not visible"

def test_page_refresh_after_registration(page: Page):
    page.goto("http://localhost:3000/?")
    page.get_by_label("First name").fill("Karthick")
    page.get_by_label("Last name").fill("Murugan")
    page.get_by_label("Email").fill("abc@example.com")
    page.get_by_role("button", name="Register", exact=True).click()
    expect(page).to_have_url("http://localhost:3000/?", timeout=5000), "Page did not refresh to the original URL"
