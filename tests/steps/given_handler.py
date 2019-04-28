# pylint: disable=E0611, E0213, R0201

"""
This file will contain all the given steps
"""

import constants
import time

from behave import given
from src.control import webdriver_control


class GivenHandler():
    """
    This class will handle all the Given Steps
    """

    @given('I try a given step')
    def i_try_a_give_step(context):
        """
        :params:
            <context>: the context of the feature
        """

    @given('I open the website "{url}" on "{device}"')
    def i_open_the_website(context, url, device):
        """
        :params:
            <context>: the context of the feature
            <url>: the given url to open
            <devices>: the given device to run
        """
        resize = context.config.userdata.get("resize")
        webdriver_control.select_webdriver(device)
        webdriver_control.open_url(url)
        if resize == 'Yes':
            constants.DRIVER.maximize_window()
            time.sleep(1)
