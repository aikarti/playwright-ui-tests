import datetime
import os
import re
import pytest
from playwright.sync_api import Page, expect

BASE_URL = "http://localhost:3000"

#@pytest.mark.parametrize("browser_name", ["chromium"])
def test_checkbox_selection(page: Page):
    os.makedirs("screenshots", exist_ok=True)

    try:
        # Navigate to base URL
        page.goto(BASE_URL)

        # ✅ Check the checkbox
        page.locator("#heard-about").check()

        # ✅ Assert checkbox is checked
        expect(page.locator("#heard-about")).to_be_checked()

        # enter text in the textbox that appears after checking the checkbox
        page.locator("#textarea").fill("Playwright")

    except AssertionError as e:
        # ✅ Capture screenshot on failure
        screenshot_path = f"screenshots/test_checkbox_{datetime.now().strftime('%Y%m%d_%H%M%S')}.p"
        page.screenshot(path=screenshot_path)
        print("Screenshot saved at:", os.path.abspath(screenshot_path))
        print(f"❌ Test failed. Screenshot saved at: {screenshot_path}")
        raise e