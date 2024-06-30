import requests
import json
import os
import pickle

url = 'https://api.youpin898.com/api/homepage/search/new/list'
keyWords = input('请输入武器名字:')

with open("person.pickle", "rb") as file:
    authorization = pickle.load(file)

# authorization = input('请输入Token:')

# 保存对象到文件
# with open("person.pickle", "wb") as file:
#     pickle.dump(authorization, file)

headers = {
    'authorization': authorization,
    'content-type': 'application/json; charset=utf-8',
}
json = {
    "keyWords": keyWords
}
r = requests.post(url, headers=headers, json=json)
data = r.json()

TotalCount = data['TotalCount']
print('查询出', TotalCount, '条信息')
a = 0
while a < TotalCount:
    CommodityName = data['Data']['commodityTemplateList'][a]['CommodityName']
    Id = data['Data']['commodityTemplateList'][a]['Id']
    Price = data['Data']['commodityTemplateList'][a]['Price']
    SteamPrice = data['Data']['commodityTemplateList'][a]['SteamPrice']

    print('饰品名字:', CommodityName, '饰品ID:', Id, '饰品价格:', Price, '饰品steam价格:', SteamPrice)
    a += 1
else:
    print('查询结束')

# print(r.text)

os.system('pause')

# data2 =[CommodityName,Id,Price,SteamPrice]
