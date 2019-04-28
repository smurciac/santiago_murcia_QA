# pylint: disable=C0411, E0213, R0201, E1101, E0611

"""
This file will contain all the then steps
"""

import allure
import constants
import random
import time

from behave import then
from src.control import helper_control, api_control
from selenium.webdriver.support.color import Color
from selenium.webdriver.common.by import By


class ThenHandler():
    """
    This class will handle all Then steps
    """

    @then('I will assert any result')
    def i_will_assert_any_result(context):
        """
        :params:
            <context>: the context of the feature
        """
        time.sleep(3)
        result = random.randint(1, 6)
        if result < 3:
            screen_name = helper_control.urlify(helper_control.datetime_now('screen')) + '.png'
            allure.attach(constants.DRIVER.get_screenshot_as_png(), name=screen_name,
                          attachment_type=allure.attachment_type.PNG)
            assert False
        else:
            assert True

    @then('I expect to see the text "{text}" on "{element}"')
    def i_expect_to_see_the_text(context, text, element):
        """
        :params:
            <context>: the context of the feature
            <text>: the given text to validate
            <element>: the element to expect the given text
        """
        target_element_text = constants.PAGE.get_element_text(element)
        assert text.lower() == target_element_text.lower(), 'The expected text was: {} but current text is: {}'.format(
            text, target_element_text)

    @then('I expect to see the "{element}"')
    def i_expect_to_see_the_element(context, element):
        """
        :params:
            <context>: the context of the feature
            <element>: the expected element
        """
        target_element = constants.PAGE.get_element(element)
        assert target_element.is_displayed(), 'The element: {} is not displayed'.format(element)
