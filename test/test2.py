from urllib import parse

urldata = "https://api.youpin898.com/api/homepage/new/es/template/GetCsGoPagedList"
# 请求头
headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2MmY0YTNlNWExMTI0MjYwYmYxNWZlZWI1Y2JhMjk4ZiIsIm5hbWVpZCI6IjMxNTIzMzIiLCJJZCI6IjMxNTIzMzIiLCJ1bmlxdWVfbmFtZSI6ImhheWh1YeS4gOWPt-S7kyIsIk5hbWUiOiJoYXlodWHkuIDlj7fku5MiLCJ2ZXJzaW9uIjoiRXExIiwibmJmIjoxNzE2NjQxNDIyLCJleHAiOjE3MTk3Mzc0MjIsImlzcyI6InlvdXBpbjg5OC5jb20iLCJkZXZpY2VJZCI6IlplNnZRWGhYcktNREFCeDlpNTZzMkw2aSIsImF1ZCI6InVzZXIifQ.o4gDgzuWzowYaXeMGC2chh_Q_MbW_mD67Hnka3h5f34',
    'Content-Type': 'application/json'
}
# 获取全部参数的键值组成字典
result = parse.urlparse(url=urldata)
query_dict = parse.parse_qs(result.query)
print(query_dict)
