from turtle import color
from urllib.request import urlopen
import json
from pprint import pprint
url = "https://random-data-api.com/api/commerce/random_commerce?size=100"
response = urlopen(url)
data = json.loads(response.read())
dic = dict()
dic["colores"] = []
dic["department"] = []
colores = []
for i in data:
    # print(i)
    if i["color"] not in dic["colores"]:
        dic["colores"].append(i["color"])
        if i["department"] not in dic["department"]:
            dic["department"].append(i["department"])

pprint(dic)
