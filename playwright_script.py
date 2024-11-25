# playwright_script.py
from playwright.sync_api import sync_playwright
import time
def run_playwright_script():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://www.google.com')
        print(page.title())
        time.sleep(100)
        browser.close()

if __name__ == "__main__":
    run_playwright_script()
