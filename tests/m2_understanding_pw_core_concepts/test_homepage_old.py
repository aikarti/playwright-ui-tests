from playwright.sync_api import sync_playwright

def test_homepage():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('http://localhost:8000/')
        browser.close()

def test_homepage2():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('http://localhost:8000/')
        browser.close()
