import requests

from bs4 import BeautifulSoup
import json

# url = "https://leagueoflegends.fandom.com/wiki/List_of_champions"
# htmldoc = requests.get(url).content
# soup = BeautifulSoup(htmldoc, "html5lib")
# champs  = {champ.find("td")["data-sort-value"]:{"wiki-link":champ.find("td").find("a")["href"]} for champ in soup.find_all("tbody")[1].find_all("tr")[1:]}
# with open("champs.json","w") as r:
#     r.write(json.dumps({"Champions":champs},indent=2))

with open("champs.json", "r") as f:
    champs = json.load(f)


#c = champs["Champions"]["Tahm Kench"]
# for c in list(champs["Champions"].values()):
#     link = c["wiki-link"]
#     url = "https://leagueoflegends.fandom.com" + link
#     print(url)
#     htmldoc = requests.get(url).content
#     soup = BeautifulSoup(htmldoc, "html5lib")

#     banner = soup.find("div",class_="FullWidthImage fxaa")
#     c["banner-link"] = banner.a["href"]
#     champ_container = soup.find("div",id="infobox-champion-container")
#     champrender=champ_container.find("figure",class_="pi-item").a["href"]

#     c["champ-render"] = champrender
#     champinfo = champ_container.find_all("div",class_="pi-item")
#     epithet = champinfo[0].find("span").text
#     c["epithet"] = epithet
#     #print(epithet)

#     champ = {}
#     for item in champinfo:
#         key = ""
#         descriptor = item.find("h3")
#         if descriptor is not None:
#             #print(descriptor.text)
#             key = descriptor.text

#         value = []
        
#         data = item.find("div",class_="pi-data-value")
#         #print(data)
#         if data is not None:
#             # print("\t"+data.text)
            
#             values = data.find_all("a")
#             a = data.find("a")
#             if a:
#                 #print(data.a.text)
#                 value.append(a.text)
#             if values:
#                 #print(values)
#                 value = [v.text for v in values]
#                 #print(values)     
#         value = [v for v in value if not v == ""]
#         if len(value) ==1:
#             value = value[0]
#         if not key == "" and not value == []:
#             champ[key]=value
#     c["Info"]=champ
#     #print(c)


# adds the different range types to these champs
# rm = ["Elise","Jayce","Gnar","Kayle","Nidalee"]

# for name,c in champs["Champions"].items():
#     #print(name,c)
#     if name in rm:
#         current = c["Info"]["Range type"]
#         if(current == "Melee"):
#             c["Info"]["Range type"] = ["Melee", "Ranged"]
#         else:
#             c["Info"]["Range type"] = ["Ranged","Melee"]
# print(banner.a["href"])

# for name,c in champs["Champions"].items():
#     if "Melee" in c["Info"]["Range type"]:
#         print(name)

# adds the positions for 
# champs["Champions"]["Rell"]["Info"]["Position(s)"] = "Support"
# champs["Champions"]["Yone"]["Info"]["Position(s)"] = ["Top","Middle"]
# champs["Champions"]["Seraphine"]["Info"]["Position(s)"] = ["Support","Middle"]

# print([name for name,c in champs["Champions"].items() if "Bottom" in c["Info"]["Position(s)"]])
# print([name for name,c in champs["Champions"].items() if "'" in name])

# for name,c in champs["Champions"].items():
#     try: 
#         a = c["Info"]["Position(s)"]
#     except:
#         print(name)
# print(type([]))
# for name,c in champs["Champions"].items():
#     info= c["Info"]
#     if("Position(s)" in info.keys() and type(info["Position(s)"]) == list):
#         print(name, info["Position(s)"])



# with open("champs.json","w") as r:
#     r.write(json.dumps(champs,indent=2))

