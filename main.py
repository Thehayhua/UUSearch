# 引入包
import Template
import Search
import time
# 请求头
headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiY2Q2ZThiNzdjOWM0ZDg3YmI1YTI5NzY5MTJhYzQyZiIsIm5hbWVpZCI6IjMxNTIzMzIiLCJJZCI6IjMxNTIzMzIiLCJ1bmlxdWVfbmFtZSI6ImhheWh1YeS4gOWPt-S7kyIsIk5hbWUiOiJoYXlodWHkuIDlj7fku5MiLCJ2ZXJzaW9uIjoid21kIiwibmJmIjoxNzE3MzIzNDE0LCJleHAiOjE3MjEzMzAyMTQsImlzcyI6InlvdXBpbjg5OC5jb20iLCJkZXZpY2VJZCI6IlpqQzZITHRyTWpNREFOUWg0WWZEUFJZUiIsImF1ZCI6InVzZXIifQ.HHAvZF8WIuk1_ONQ83nSBHTruI3l2oURi0q_pEnd_ew',
    'Content-Type': 'application/json'
}
number = input('请输入选择编号(1.匕首,2.手枪,3.步枪,4.微型冲锋枪,5.霰弹枪,6.机枪,7.手套,8.印花):')
Price = input('所需价格：')
Type = ['CSGO_Type_Knife_Unlimited',
        'CSGO_Type_Pistol_Unlimited',
        'CSGO_Type_Rifle_Unlimited',
        'CSGO_Type_SMG_Unlimited',
        'CSGO_Type_Shotgun_Unlimited',
        'CSGO_Type_Machinegun_Unlimited',
        'Type_Hands_Unlimited',
        'CSGO_Tool_Sticker_Unlimited'
        ]

json = {
    "filterMap": {
        "Type": [
            Type[int(number) - 1]
        ]
    },
    "gameId": 730,
    "listSortType": 0,
    "listType": 10,
    "maxPrice": Price,
    "pageIndex": 1,
    "pageSize": 100,
    "sortType": 0,
    "stickerAbrade": 0,
    "stickersIsSort": 'false',
    "Sessionid": "ZjC6HLtrMjMDANQh4YfDPRYR"
}


counter = 0

data = Template.Template(headers, json)

print(data)



#     sheetTemplateId = data['Data']['CommodityList'][0]['TemplateId']
#     sheetCommodityName = data['Data']['CommodityList'][0]['CommodityName']
#     sheetPrice = data['Data']['CommodityList'][0]['Price']
#     sheetTypeName = data['Data']['TemplateInfo']['TypeName']
#     sheetExterior = data['Data']['TemplateInfo']['Exterior']
#     sheetRarity = data['Data']['TemplateInfo']['Rarity']
#     # 悠悠写入execl
#     file_path = 'UU.xlsx'
#     sheet_name = 'Sheet1'
#     workbook = load_workbook(file_path)
#     sheet = workbook[sheet_name]
#
#     # market(10262)
#     data = [sheetTemplateId, sheetCommodityName, sheetPrice, sheetTypeName, sheetExterior, sheetRarity]
#     sheet.append(data)
#     workbook.save(file_path)
#
#
# counter = 44
#
# while True:
#     try:
#         market(counter)
#         time.sleep(random.randint(8, 10))
#         counter += 1
#         print(counter)
#     except TypeError:
#         print('第' + str(counter + 1) + '次参数错误')
#         counter += 1

# TemplateId= data['Data']['CommodityList'][0]['TemplateId']
# CommodityName=data['Data']['CommodityList'][0]['CommodityName']
# Price=data['Data']['CommodityList'][0]['Price']

# 悠悠写入execl
# file_path = 'UU.xlsx'
# sheet_name = 'Sheet1'
# workbook = load_workbook(file_path)
# sheet = workbook[sheet_name]
# sheet['A1'] ='templateId'
# sheet['B1'] ='CommodityName'
# sheet['C1'] ='Price'
# sheet['A2'] = TemplateId
# sheet['B2'] =CommodityName
# sheet['C2'] =Price
#
# workbook.save(file_path)
