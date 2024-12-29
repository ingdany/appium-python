import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
import logging
from urllib3.exceptions import MaxRetryError
from appium.webdriver.appium_connection import AppiumConnection
from appium.webdriver.appium_service import AppiumService

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture(scope="class")
def driver(request):
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "uiautomator2"
    options.device_name = "POCO X3 NFC"
    options.app_package = "com.android.settings"
    options.app_activity = ".Settings"
    options.language = "en"
    options.locale = "US"

    appium_service = AppiumService()
    appium_service.start()

    try:
        logger.info("Attempting to connect to Appium server...")
        driver = webdriver.Remote("http://localhost:4723", options=options)
        request.cls.driver = driver
        logger.info("Successfully connected to Appium server")
        yield driver
    except MaxRetryError:
        logger.error("Failed to connect to Appium server. Is it running?")
        raise
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise
    finally:
        if "driver" in locals():
            driver.quit()
