import pytest
from appium import webdriver
from pages.settings_page import SettingsPage


@pytest.mark.usefixtures("driver")
class TestAppium:

    def test_find_title(self, driver):
        settings_page = SettingsPage(driver)
        settings_page.find_title()


if __name__ == "__main__":
    pytest.main(["-v", "tests/android_settings_pytest.py"])
