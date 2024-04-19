import requests 
from bs4 import BeautifulSoup
import json
import re

with open("items.json", "r") as r:
    items = json.load(r)

query = {}


for name,item in list(items["Items"].items()):
    a = "Stats"
    search = "ability power"
    if(a in item["Info"] and search in item["Info"][a] and  item["Type"]=="Mythic items"):
        query[name] = item["Info"][a][search]
        #print({name: })
print(sorted(query.items(),key=lambda x:x[1],reverse=True)[:5])
        

# for name,item in list(items["Items"].items())[:]:
#     # if not "Info" in item.keys():
#     #     item["Info"]= {}
#     #     print("No info: " + name)

#     # else:
#     #     if not "Stats" in item["Info"].keys():
#     #         item["Info"]["Stats"] = []
#     #         print("No stats: " + name)
#     #     else:
#     stats = [stats for stats in item["Info"]["Stats"]]
#     new_stat = {}
#     for stat in stats:
#         value = None
#         key = None

#         if stat.startswith("+ "):

#             value = stat[1:3].replace(" ", "")
#             if value.isnumeric():
#                 value = int(value)
#             key = "Gold " +stat[4:]
#             #print(value,rest)
#         elif(stat.startswith("+")):
#             #print(stat)
#             if " " in stat:
#                 space = stat.index(" ")
                
#                 value = (stat[1:space])
#                 if value.isnumeric():
#                     value = int(value)
#                 key = stat[1+space:]
#         new_stat[key] = value

#         if(key and value):
#             item["Info"]["Stats"] = new_stat
#             #print(new_stat)
            
#             #print("gold item", name)
    
#     #print(stats)
    
# with open("temp.json","w") as r:
#     r.write(json.dumps(items, indent=2))