# playwright_script.py
from playwright.sync_api import sync_playwright
import time
import subprocess
import pyautogui

def open_notebook():
    subprocess.Popen('notepad.exe')
    time.sleep(2)
    pyautogui.typewrite('IA-Tesing from Shanghai')
    pyautogui.press('enter')
    pyautogui.hotkey('alt', 'f4')
    time.sleep(2)
    pyautogui.press('n')

def run_playwright_script():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://www.baidu.com')
        page.fill("input[name='wd']", "Volvo")
        page.click("input[type='submit']")
        page.wait_for_selector("#content_left")
        print(page.title())
        time.sleep(100)
        browser.close()

if __name__ == "__main__":
    open_notebook()
    run_playwright_script()
