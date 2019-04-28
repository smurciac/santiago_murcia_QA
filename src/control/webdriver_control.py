# pylint: disable=C0411

"""
This file contain all the webdriver configurations
"""

import constants
import tkinter

from selenium import webdriver as selenium_webdriver
from appium import webdriver as appium_webdriver


def select_webdriver(device):
    """
    :params:
        <device>: device to start the corresponding driver
    """
    if device.lower() == "chrome":
        constants.DRIVER = selenium_webdriver.Chrome()
    if device.lower() == "firefox":
        constants.DRIVER = selenium_webdriver.Firefox()
    if device.lower() == "safari":
        constants.DRIVER = selenium_webdriver.Safari()
    if device.lower() == "iphone":
        constants.DRIVER = appium_webdriver.Remote(
            constants.APPIUM_SERVER, constants.IPHONE_DESIRED_CAPS)
    if device.lower() == "android":
        constants.DRIVER = appium_webdriver.Remote(
            constants.APPIUM_SERVER, constants.ANDROID_DESIRED_CAPS)
    constants.DEVICE = device


def open_url(url):
    """
    :params:
        <url>: the url to be open
    """
    if constants.DEVICE.lower():
        constants.DRIVER.get(url)
    constants.URL = url


def set_windows_size(device, size):
    """
    :params:
        <device>: the given device to run
        <size>: the given size to set the device
    """
    screen = tkinter.Tk()
    if device.lower() != "android" and device.lower() != "iphone":
        if device.lower() == "safari" or size == 0:
            constants.DRIVER.maximize_window()
        else:
            constants.DRIVER.set_window_position(0, 0)
            constants.DRIVER.set_window_size(size, screen.winfo_screenheight())
