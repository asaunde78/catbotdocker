import requests 
from bs4 import BeautifulSoup
import json
#import imagemagick
# url = "https://leagueoflegends.fandom.com/wiki/Item_(League_of_Legends)"
#htmldoc = requests.get(url).content.decode("utf-8")
# soup = BeautifulSoup(requests.get(url).content, 'html5lib')

# grid = soup.find_all("div",id="item-grid")[1]
# categories = grid.find_all("dl")
# categories = [cat.text for cat in categories]
# item_groups = grid.find_all("div",class_="tlist")
# item_groups = [group.find_all("li") for group in item_groups]
# I = [[item.a["href"]for item in items] for items in item_groups]

# d = {"Items":{}}
# for index, group in enumerate(I):
#     key = "Type"
#     value = categories[index]
#     for item in group:
#         d["Items"][item] = {}
#         d["Items"][item]["wiki-link"] = item
#         d["Items"][item][key]=value
# # print(d)
# with open("items.json", "w") as r:
#     r.write(json.dumps(d,indent=2))
#print(len(I),len(categories))

with open("items.json", "r") as r:
    items = json.load(r)

# bad_types = ["Ornn's Mythic item upgrades","Champion exclusive items","Minion and Turret items","Removed items"]
# for i,item in list(items["Items"].items())[::-1]:
#     if item["Type"] in bad_types:
#         continue
#     url = "https://leagueoflegends.fandom.com" + item["wiki-link"]
#     r = requests.get(url).content
#     soup = BeautifulSoup(r,"html5lib")
    
#     box = soup.find("aside", role="region", class_="portable-infobox")
#     if(box):
#         name = box.find("h2",class_="pi-item")
#         if(name):
#             name = name.find_all(string=True)[0]
#         else:
#             name = "Different Wiki Page Style"
#     else:
#         name = "Different Wiki Page Style"
#     print(name)
#     #better = {name:item.values()}
#     if(i == item["wiki-link"]):
#         items["Items"][name] = items["Items"][i] 
#         del items["Items"][i]
    
    #print(better)
# count = 0
# for name,item in list(items["Items"].items())[::-1]:
#     if(name == item["wiki-link"]):
#         del items["Items"][name]

# items["Items"] = dict(sorted(items["Items"].items()))
#print(items)
with open("temp.json","w") as r:
    r.write(json.dumps(items, indent=2))
    #print(name)