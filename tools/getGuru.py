#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File   : getGuru.py    
@Author : Susie
@Create : 2022/8/30 下午8:33
@Desc   : 
"""
import requests

url = "https://api.apis.guru/v2/list.json"

payload={}
headers = {
   'authority': 'api.apis.guru',
   'accept': 'application/json, text/javascript, */*; q=0.01',
   'accept-language': 'zh,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7',
   'if-modified-since': 'Sat, 27 Aug 2022 01:00:33 GMT',
   'if-none-match': 'W/"63096cb1-555824"',
   'origin': 'https://apis.guru',
   'referer': 'https://apis.guru/',
   'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
   'sec-ch-ua-mobile': '?0',
   'sec-ch-ua-platform': '"macOS"',
   'sec-fetch-dest': 'empty',
   'sec-fetch-mode': 'cors',
   'sec-fetch-site': 'same-site',
   'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)
print(typeof(response))
print(response.text)
