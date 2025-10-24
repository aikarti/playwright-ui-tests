from playwright.sync_api import sync_playwright, expect, Page
from tests.utils.constants import BASE_URL


def test_select(page):
    # Navigate to the savings page
    page.goto(f'{BASE_URL}/savings.html')   

    # Get the input elements
    deposit = page.get_by_test_id('deposit')
    period = page.get_by_test_id('period')
    result = page.get_by_test_id('result')

    # Select deposit amount
    deposit.fill('2000')
    expect(deposit).to_have_value('2000')
    # Select period
    period.select_option('1 Year')
    expect(period).to_have_value('1 Year')
    # Verify the result
    expect(result).to_have_text('After 1 Year you will earn $100.00 on your deposit')
    print("✅ test_select passed successfully.")



def test_select_one():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # 👈 This makes the browser visible
        page = browser.new_page()

        page.goto("http://localhost:3000/savings.html")

        deposit = page.get_by_test_id('deposit')
        period = page.get_by_test_id('period')
        result = page.get_by_test_id('result')

        deposit.fill('2000')
        expect(deposit).to_have_value('2000')

        #period.fill('1 Year')
        period.select_option('1 Year')
        expect(period).to_have_value('1 Year')

        expect(result).to_have_text('After 1 Year you will earn $100.00 on your deposit')

        print("✅ test_select passed successfully.")
        page.pause
        #browser.close()