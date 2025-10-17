from playwright.sync_api import sync_playwright

#with sync_playwright() as p:
#       browser = browser_type.launch(headless=False, slow_mo=1000)
#       page = browser.new_page()
#        page.goto("https://whatsmybrowser.org/")
#        page.screenshot(path=f"example-{browser_type.name}.png")
#        browser.close()
#
#        from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    for browser_type in [p.chromium, p.firefox, p.webkit]:
        try:
            browser = browser_type.launch(headless=False, slow_mo=1000)
            page = browser.new_page()
            page.goto("https://whatsmybrowser.org/")
            page.screenshot(path=f"example-{browser_type.name}.png")
            print(f"Screenshot saved for {browser_type.name}")
        except Exception as e:
            print(f"Error with {browser_type.name}: {e}")
        finally:
            browser.close()



