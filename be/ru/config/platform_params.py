# ETCP platform
etcp_headers = {
  'Host': 'ife.etcp.cn',
  'Content-Type': 'application/json',
  't': '1607429454',
  'Accept-Encoding': 'gzip, deflate, br',
  'Connection': 'keep-alive',
  'Accept': '*/*',
  'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.17(0x1700112a) NetType/WIFI Language/zh_CN',
  'Referer': 'https://servicewechat.com/wxc07f9d67923d676d/199/page-frame.html',
  's': '0B44B667C97B1386E00742B4FCE642B6',
  'Accept-Language': 'zh-cn',
}

etcp_params = {
  'version': '5.5.0',
  'userId': '',
  'token': '',
  'paySource': '34',
  'carId': '',
  'payWay': '2',
  'payFrom': '58',
  'couponCode': '',
  'carNumber': '川AUUUUU',
  'privacyStatus': '1',
}

etcp_url = 'https://ife.etcp.cn/api/v2/parking/get-park-fee'

# stop where platform
stop_where_headers = {
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

stop_where_body = {
  "REQUESTS": [
    {
      "REQ_COMM_DATA": {
        "car_id": "00000",
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

stop_where_url = 'https://mpapi.tnar.cn/kesb_req'
