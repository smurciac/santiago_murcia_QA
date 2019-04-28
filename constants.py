# pylint: disable=C0330

"""
This file will keep all the constants used over the framework
"""

import os

APPIUM_DRIVER = os.path.dirname(os.path.abspath("drivers")) + "/drivers"
APPIUM_SERVER = "http://127.0.0.1:4723/wd/hub"
DEVICE = None
DRIVER = None
PAGE = None
URL = ""

IPHONE_DESIRED_CAPS = {
    "platformName": "iOS",
    "platformVersion": "12.1",
    "automationName": "XCUITest",
    "deviceName": "iPhone XS",
    # "app": "",
    "browserName": "Safari"
    # "fullReset": True,
    # "noReset": False
}

ANDROID_DESIRED_CAPS = {
    "platformName": "Android",
    "platformVersion": "7.1.1",
    "automationName": "uiautomator2",
    "deviceName": "Nexus_6",
    "avd": "Nexus_6",
    # "app": "",
    "browserName": "Chrome",
    "chromedriverExecutableDir": APPIUM_DRIVER
    # "fullReset": True,
    # "noReset": False
}
