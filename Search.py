import requests

url ='https://api.youpin898.com/api/homepage/search/new/list'
def Search(url,headers,json):
    Search= requests.post(url=url,headers=headers,json=json)
    print(Search.text)