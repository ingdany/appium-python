from appium.webdriver.common.appiumby import AppiumBy
from pages.utils.base_page_object import BasePageObject


class SettingsPage(BasePageObject):
    def __init__(self, driver):
        super().__init__(driver)
        self.settings_title = (AppiumBy.XPATH, '//*[@text="Settings"]')

    def find_title(self):
        self.click_element(self.settings_title)
