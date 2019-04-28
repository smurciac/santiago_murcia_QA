# pylint: disable=C0411, E0213, R0201, E1101, E0611

"""
This file will contain all the when steps
"""

import constants
import time

from behave import when
from src.control import webdriver_control


class WhenHandler():
    """
    This class will handle all When steps
    """

    @when("I perform some other action")
    def i_perform_some_other_action(context):
        """
        :params:
            <context>: the context of the feature
        """

    @when('I set the "{device}" windows size to "{size:d}" pixels')
    def i_set_the_windows_size(context, device, size):
        """
        :params:
            <context>: the context of the feature
            <device>: the given device to run
            <size>: the given size to set the device
        """
        webdriver_control.set_windows_size(device, size)
        time.sleep(1)

    @when('I click the "{element}"')
    def i_click_element(context, element):
        """
        :params:
            <context>: the context of the feature
            <element>: the element to execute the action
        """
        element = constants.PAGE.get_element(element)
        constants.PAGE.click_element(element)

    @when('I enter the email "{email}"')
    def i_enter_the_email(context, email):
        """
        :params:
            <context>: the context of the feature
            <email>: the email to type
        """
        element = constants.PAGE.get_element('USERNAME')
        element.send_keys(email)
        time.sleep(1)

    @when('I enter the password "{password}"')
    def i_enter_the_password(context, password):
        """
        :params:
            <context>: the context of the feature
            <password>: the password to type
        """
        element = constants.PAGE.get_element('PASSWORD')
        element.send_keys(password)
        time.sleep(1)
