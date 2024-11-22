from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

class TabManager:
    def __init__(self, driver_path, enable_devtools=False):
        # Use Service to initialize WebDriver
        chrome_options = Options()
        if enable_devtools:
            chrome_options.add_argument("--auto-open-devtools-for-tabs")  # Open DevTools by default
        service = Service(driver_path)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.get("about:blank")  # Start with a blank page

    def open_tabs(self, urls):
        """Open a list of URLs in new tabs."""
        if not urls:
            print("No URLs provided to open.")
            return
        
        for index, url in enumerate(urls):
            if index == 0:
                # Load the first URL in the current tab
                self.driver.get(url)
            else:
                # Open new tabs for the remaining URLs
                self.driver.execute_script(f"window.open('{url}', '_blank');")
        
        self.driver.switch_to.window(self.driver.window_handles[0])  # Focus on the first tab

    def scroll_page(self, delay):
        """Scroll the current page."""
        try:
            scroll_height = self.driver.execute_script("return document.body.scrollHeight")
            for i in range(0, scroll_height, 500):
                self.driver.execute_script(f"window.scrollTo(0, {i});")
                time.sleep(delay)
        except Exception as e:
            print(f"Error while scrolling: {e}")

    def switch_tabs_and_scroll(self, delay_between_tabs, scroll_delay, screen_time):
        """Switch between tabs, scroll through each page, and keep tabs open."""
        tabs = self.driver.window_handles
        if not tabs:
            print("No tabs found to switch.")
            return

        for tab in tabs:
            self.driver.switch_to.window(tab)
            current_url = self.driver.current_url
            if current_url == "data:,":
                print("Skipping blank tab.")
                continue  # Skip blank tabs
            print(f"Current Tab: {current_url}")
            self.scroll_page(scroll_delay)
            time.sleep(screen_time)  # Keep the tab open for specified screen time
            time.sleep(delay_between_tabs)

    def enable_devtools_logging(self):
        """Enable developer tools logging (e.g., console logs)."""
        try:
            self.driver.execute_cdp_cmd("Log.enable", {})
        except Exception as e:
            print(f"Error enabling DevTools logging: {e}")

    def fetch_console_logs(self):
        """Fetch and print console logs from DevTools."""
        try:
            logs = self.driver.execute_cdp_cmd("Log.get", {})
            print(f"Console Logs: {logs}")
        except Exception as e:
            print(f"Error fetching console logs: {e}")

    def close_browser(self):
        """Close the browser."""
        try:
            self.driver.quit()
        except Exception as e:
            print(f"Error while closing the browser: {e}")
