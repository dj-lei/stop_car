import gzip
import base64
from PIL import Image
from io import BytesIO
import requests


def query_dict(key, value):
    doc = {
        "query": {
            "term": {
                key: str.lower(value)
            }
        }
    }
    return doc


def query_with(kv):
    doc = {
            "query": {
                "bool": {
                    "must": []
                }
            }
        }
    for k, v in kv:
        doc["query"]["bool"]["must"].append({"term": {k: v}})
    return doc


def image_to_base64(image_path):
    pic = Image.open(image_path)
    pic = pic.convert('RGB')
    w, h = pic.size
    if w > 800:
        pic = pic.resize((800, int(h / (w / 800))), Image.ANTIALIAS)
    else:
        pic = pic.resize((w, h), Image.ANTIALIAS)
    output_buffer = BytesIO()
    pic.save(output_buffer, format='JPEG', quality=50)
    byte_data = output_buffer.getvalue()
    base64_str = base64.b64encode(byte_data)
    return base64_str.decode()


def base64_to_image(base64_str):
    byte_data = base64.b64decode(base64_str)
    image_data = BytesIO(byte_data)
    img = Image.open(image_data)
    return img


def file_compress(file):
    return gzip.compress(file)


def file_decompress(file):
    return gzip.decompress(eval(file))


def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").json()

def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))

# your spider code

def getHtml(url,headers,params):
    # ....
    retry_count = 5
    proxy = get_proxy().get("proxy")
    while retry_count > 0:
        try:
            html = requests.get(url, headers=headers, params=params, proxies={"http": "http://{}".format(proxy)})
            # 使用代理访问
            return html
        except Exception:
            retry_count -= 1
    # 删除代理池中代理
    delete_proxy(proxy)
    return None


etcp_headers = {
    'Host':'ife.etcp.cn',
    'Content-Type':'application/json',
    't':'1607429454',
    'Accept-Encoding':'gzip, deflate, br',
    'Connection':'keep-alive',
    'Accept':'*/*',
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.17(0x1700112a) NetType/WIFI Language/zh_CN',
    'Referer':'https://servicewechat.com/wxc07f9d67923d676d/199/page-frame.html',
    's':'0B44B667C97B1386E00742B4FCE642B6',
    'Accept-Language':'zh-cn',
}

etcp_params = {
    'version':'5.5.0',
    'userId':'',
    'token':'',
    'paySource':'34',
    'carId':'',
    'payWay':'2',
    'payFrom':'58',
    'couponCode':'',
    'carNumber':'川AU2U79',
    'privacyStatus':'1',
}

etcp_url = 'https://ife.etcp.cn/api/v2/parking/get-park-fee'

where_headers = {
    'Host': 'mpapi.tnar.cn',
    'Content-Type': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.17(0x1700112a) NetType/WIFI Language/zh_CN',
    'Referer': 'https://servicewechat.com/wx1a2fa4c3ff332d32/101/page-frame.html',
    'Content-Length': '137',
    'Accept-Language': 'zh-cn',
}

where_body = {
  "REQUESTS": [
    {
      "REQ_COMM_DATA": {
        "car_id": "03Y26",
        "cartype": "0",
        "park_code": "",
        "third_type": "3"
      },
      "REQ_MSG_HDR": {
        "SERVICE_ID": "87202011"
      }
    }
  ]
}

where_url = 'https://mpapi.tnar.cn/kesb_req'