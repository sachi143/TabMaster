import unittest
from selenium import webdriver
from src.browser.tab_manager import TabManager
from config.settings import DRIVER_PATH

class TestTabManager(unittest.TestCase):
    def setUp(self):
        self.tab_manager = TabManager(DRIVER_PATH)

    def test_open_tabs(self):
        urls = ["https://example.com", "https://example.org"]
        self.tab_manager.open_tabs(urls)
        tabs = self.tab_manager.driver.window_handles
        self.assertEqual(len(tabs), len(urls))

    def tearDown(self):
        self.tab_manager.close_browser()

if __name__ == "__main__":
    unittest.main()
