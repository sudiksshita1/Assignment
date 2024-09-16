import os

class Config:
    # Base URL for SauceDemo application
    BASE_URL = "https://www.saucedemo.com"

    # Test User credentials
    USERNAME = "standard_user"
    PASSWORD = "secret_sauce"

    # Browser configurations
    BROWSER = os.getenv("BROWSER", "chrome")  # Default to Chrome if not specified

    # WebDriver configuration
    CHROME_DRIVER_PATH = os.getenv("CHROME_DRIVER_PATH", "./drivers/chromedriver")
    FIREFOX_DRIVER_PATH = os.getenv("FIREFOX_DRIVER_PATH", "./drivers/geckodriver")

    # Allure report configuration
    ALLURE_REPORT_DIR = "./reports/allure_reports"

    # Timeout settings
    PAGE_LOAD_TIMEOUT = 30
    IMPLICIT_WAIT = 10

    @staticmethod
    def get_browser_options():
        """Return browser options based on the configuration."""
        from selenium.webdriver.chrome.options import Options as ChromeOptions
        from selenium.webdriver.firefox.options import Options as FirefoxOptions

        if Config.BROWSER == "chrome":
            options = ChromeOptions()
            options.add_argument("--headless")  # Run Chrome in headless mode
            return options
        elif Config.BROWSER == "firefox":
            options = FirefoxOptions()
            options.add_argument("--headless")  # Run Firefox in headless mode
            return options
        else:
            raise ValueError(f"Unsupported browser: {Config.BROWSER}")

# config/config.py
