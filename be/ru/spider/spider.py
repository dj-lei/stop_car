from ru.spider import *
from ru.views import *


def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").json()


def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))


def get_html(url, headers, params, proxy, request_type='GET'):
    retry_count = 5
    while retry_count > 0:
        try:
            if request_type == 'GET':
                html = requests.get(url, headers=headers, params=params, proxies={"http": "http://{}".format(proxy)})
            elif request_type == 'POST':
                html = requests.post(url, headers=headers, data=json.dumps(params), proxies={"http": "http://{}".format(proxy)})
            return html
        except Exception:
            retry_count -= 1
    delete_proxy(proxy)
    return None


