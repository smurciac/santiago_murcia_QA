# pylint: disable=E501
"""
This file will contain all Home elements and actions
"""

from src.pages.main_page import MainPage
from selenium.webdriver.common.by import By


class SignInPage(MainPage):
    """
    This class has all Home elements and actions
    """
    def __init__(self):
        super(SignInPage, self).__init__()
        self.elements = {
            'USERNAME': (By.CSS_SELECTOR, '#username'),
            'PASSWORD': (By.CSS_SELECTOR, '#password'),
            'SIGNIN': (By.CSS_SELECTOR, '[ng-bind*="SIGN IN"]'),
            'WARNING': (By.CSS_SELECTOR, '[ng-bind*="error.message"]')
        }

    def __del__(self):
        pass
