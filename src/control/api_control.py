# pylint: disable=C0411

"""
This file contain some api methods
"""

import constants
import requests


def get_data(api):
    """
    :params:
        <api>: the endpoint to get the data
    """
    URL = 'http://some/api/{}'.format(api)
    PARAMS = {}
    response = requests.get(url=URL, params=PARAMS)
    return response.json()
