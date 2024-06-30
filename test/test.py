import openpyxl
from openpyxl import load_workbook
import requests
import json
import time

# 请求地址
Host = 'https://api.youpin898.com/api/homepage/new/es/template/GetCsGoPagedList'

# 请求头
headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJkMDM3OTQ2YjVkNWI0YTg1YjMyMTk1MDY2NzkyOWI3YyIsIm5hbWVpZCI6IjMyNTA1NjgiLCJJZCI6IjMyNTA1NjgiLCJ1bmlxdWVfbmFtZSI6IuWwj-eIseWQjOWtpiIsIk5hbWUiOiLlsI_niLHlkIzlraYiLCJ2ZXJzaW9uIjoieUNqIiwibmJmIjoxNzE0NDY5NDc3LCJleHAiOjE3MTk1ODE0NzcsImlzcyI6InlvdXBpbjg5OC5jb20iLCJkZXZpY2VJZCI6IlpqQzZITHRyTWpNREFOUWg0WWZEUFJZUiIsImF1ZCI6InVzZXIifQ.FWR3Oap8lP6b8A2UdLXMJFWoNUnARkpQ-sPP90BQueY',
    'Content-Type': 'application/json'
}

pageIndex = 4

json={
  "filterMap": {
    "Type": [
      "CSGO_Tool_Sticker_Unlimited"
    ]
  },
  "gameId": 730,
  "listSortType": 0,
  "listType": 10,
  "maxPrice": "0.02",
  "pageIndex": pageIndex,
  "pageSize": 100,
  "sortType": 0,
  "stickerAbrade": 0,
  "stickersIsSort": 'false',
  "Sessionid": "ZjC6HLtrMjMDANQh4YfDPRYR"
}

r= requests.post(url=Host,headers=headers,json=json)
data = r.json()



for index, value in enumerate(data['Data']):
   databc = data['Data'][index]['Id']


   print(databc)









