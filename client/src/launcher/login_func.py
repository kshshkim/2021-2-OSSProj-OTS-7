import requests

from ..consts.urls import URLS


def request_login(login_id: str, pw: str) -> dict:
    res = requests.post(url=URLS.login_url,
                        json={'name': login_id,
                              'password': pw})
    if res.status_code != 200:
        res = requests.post(url=URLS.login_url,
                            data={'name': login_id,
                                  'password': pw})
    return res.json()
