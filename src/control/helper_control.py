# pylint: disable=C0411

"""
This file contain some helper methods
"""

import constants
import datetime
import re
import time

from selenium.webdriver.support.color import Color


def urlify(name):
    """
    :params:
        <name>: name to be treated
    """
    name = re.sub(r"[^\w\s]", '', name)
    name = re.sub(r"\s+", '-', name)
    return name


def datetime_now(prefix):
    """
    :params:
        <prefix>: prefix to be added
    """
    symbols = str(datetime.datetime.now())
    return prefix + "-" + "".join(symbols)


def set_avd_device(avd_device):
    """
    :params:
        <avd_device>: avd device to set for android
    """
    if avd_device != 'default':
        constants.ANDROID_DESIRED_CAPS.update({"avd": avd_device})
        constants.ANDROID_DESIRED_CAPS.update({"deviceName": avd_device})


def list_element_properties(element):
    """
    :params:
        <element>: element to extract properties
    """
    html = element.get_attribute("innerHTML")
    pattern = """([a-z]+-?[a-z]+_?)='?"?"""
    return re.findall(pattern, html)
