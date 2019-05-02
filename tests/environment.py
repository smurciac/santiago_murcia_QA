# pylint: skip-file
"""
This file will contain all the methods to control the features
"""

import allure
import constants
import time

from src.control import helper_control


def before_all(context):
    """
    All actions performed before all
    """
    avd_device = context.config.userdata.get("avd_device")
    helper_control.set_avd_device(avd_device)


def before_feature(context, feature):
    """
    All actions performed before the feature
    """
    from src.pages.sign_in_page import SignInPage

    if feature.tags[0] in locals():
        clazz = locals()[feature.tags[0]]
        constants.PAGE = clazz()


def after_feature(context, feature):
    """
    All actions performed after the feature
    """
    del constants.PAGE


def before_scenario(context, scenario):
    """
    All actions performed before the scenario
    """


def after_scenario(context, scenario):
    """
    All actions performed before the scenario
    """
    constants.DRIVER.quit()


def before_tag(context, tag):
    """
    All actions performed before a tag
    """


def after_tag(context, tag):
    """
    All actions performed after a tag
    """


def before_step(context, step):
    """
    All actions performed before a step
    """


def after_step(context, step):
    """
    All actions performed after a step
    """
    time.sleep(constants.WAIT_TIME)
    if step.status == "failed":
        screen_name = helper_control.urlify(helper_control.datetime_now('screen')) + '.png'
        allure.attach(constants.DRIVER.get_screenshot_as_png(), name=screen_name,
                      attachment_type=allure.attachment_type.PNG)
