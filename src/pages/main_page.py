# pylint: disable=E1101, C0411

"""
This file will contain all Main Page elements and actions
"""

import constants
import time

from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchAttributeException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class MainPage:
    """
    This class has all Main Page elements and actions
    """

    def __init__(self):
        pass

    def get_element(self, element):
        """
        :params:
            <element>: the element to get
        """
        try:
            return constants.DRIVER.find_element(*(self.elements[element]))
        except NoSuchElementException:
            assert False, \
                "The elements: {} with locator: {} was not found.".format(
                    element, *(self.elements[element]))

    def get_elements(self, element):
        """
        :params:
            <element>: the element to get
        """
        try:
            return constants.DRIVER.find_elements(*(self.elements[element]))
        except NoSuchElementException:
            assert False, \
                "The elements: {} with locator: {} was not found.".format(
                    element, *(self.elements[element]))

    def get_element_text(self, element):
        """
        :params:
            <element>: the element to get it's text
        """
        try:
            return constants.DRIVER.find_element(*(self.elements[element])).get_attribute('textContent')
        except NoSuchAttributeException:
            assert False, "The element: {} doesn't have a text".format(element)

    @staticmethod
    def click_element(element):
        """
        :params:
            <element>: the element to click
        """
        try:
            element.click()
            time.sleep(1)
        except ElementNotInteractableException:
            assert False, \
                "The element: {} can't be clicked".format(element)
