from appium import webdriver
from appium.common.exceptions import WebDriverException
import logging


# Configure logging
logging.basicConfig(level=logging.DEBUG)

desired_caps = {
    "platformName": "Android",
    "platformVersion": "12",  # Replace with your actual Android version
    "deviceName": "POCO X3 NFC",  # Replace with your device name or ID
    "appPackage": "com.miui.calculator",
    "appActivity": "com.miui.calculator.cal.CalculatorActivity",
    "automationName": "UiAutomator2",
    "udid": "b11769",
}

# Log the desired capabilities
logging.debug(f"Desired Capabilities: {desired_caps}")

if desired_caps:
    try:
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    except WebDriverException as e:
        print(f"Error initializing webdriver: {e}")
else:
    logging.error("Desired capabilities are None")
