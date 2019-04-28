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

    r = requests.get(url=URL, params=PARAMS)
    data = r.json()
    return data['data']
