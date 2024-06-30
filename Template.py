import requests
import json
url='https://api.youpin898.com/api/homepage/new/es/template/GetCsGoPagedList'
def Template(headers,json):
    Template= requests.post(url=url,headers=headers,json=json)
    Templatedata=Template.json()
    sheetTemplateId = Templatedata['Data'][0]['Id']
    sheetCommodityName = Templatedata['Data'][0]['CommodityName']
    sheetPrice = Templatedata['Data'][0]['Price']
    sheetTypeName = Templatedata['Data'][0]['TypeName']
    sheetExterior = Templatedata['Data'][0]['Exterior']
    sheetRarity = Templatedata['Data'][0]['Rarity']
    print(sheetTemplateId,sheetCommodityName,sheetPrice,sheetTypeName,sheetExterior,sheetRarity)
    print(Template.text)