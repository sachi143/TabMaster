class DevToolsHandler:
    def __init__(self, driver):
        self.driver = driver

    def enable_logging(self):
        """Enable DevTools logging."""
        try:
            self.driver.execute_cdp_cmd("Log.enable", {})
        except Exception as e:
            print(f"Error enabling DevTools logging: {e}")

    def fetch_console_logs(self):
        """Fetch and print console logs."""
        try:
            logs = self.driver.execute_cdp_cmd("Log.get", {})
            print(f"Console Logs: {logs}")
        except Exception as e:
            print(f"Error fetching console logs: {e}")
