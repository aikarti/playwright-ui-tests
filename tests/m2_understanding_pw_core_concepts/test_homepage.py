from playwright.sync_api import sync_playwright, Page, expect
from tests.utils.constants import BASE_URL

def test_homepage(page: Page):
    page.goto(BASE_URL)
    header = page.get_by_text("Register to become a member")
    #assert header.inner_text() == "Register to become a member"
    expect(header).to_be_visible()

def test_homepage_header(page: Page):
    page.goto(BASE_URL)
    expect(page).to_have_title("Credit Association")