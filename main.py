from config.settings import DRIVER_PATH, TAB_URLS, SCROLL_DELAY, SWITCH_TAB_DELAY, SCREEN_TIME
from src.browser.tab_manager import TabManager
from src.browser.devtools_handler import DevToolsHandler
from src.utils import setup_logger
import os

# Setup logging
logger = setup_logger("logs/app.log")

def main():
    logger.info("Starting TabMaster...")

    # Initialize TabManager and DevToolsHandler
    tab_manager = TabManager(DRIVER_PATH, enable_devtools=True)
    devtools_handler = DevToolsHandler(tab_manager.driver)
    
    try:
        # Open tabs
        logger.info("Opening tabs...")
        tab_manager.open_tabs(TAB_URLS)

        # Enable DevTools logging
        logger.info("Enabling DevTools logging...")
        devtools_handler.enable_logging()

        # Dynamically fetch screen time
        dynamic_screen_time = int(os.getenv("SCREEN_TIME", SCREEN_TIME))  # Default to SCREEN_TIME if not set
        logger.info(f"Using screen time: {dynamic_screen_time} seconds")

        # Switch tabs, scroll, and wait
        logger.info("Switching between tabs and scrolling...")
        tab_manager.switch_tabs_and_scroll(SWITCH_TAB_DELAY, SCROLL_DELAY, dynamic_screen_time)

        # Fetch and print DevTools logs
        logger.info("Fetching console logs from DevTools...")
        devtools_handler.fetch_console_logs()
    except Exception as e:
        logger.error(f"An error occurred during execution: {e}")
    finally:
        # Close the browser
        tab_manager.close_browser()
        logger.info("TabMaster finished.")

if __name__ == "__main__":
    main()
