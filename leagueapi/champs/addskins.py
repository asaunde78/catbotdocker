import json 
from bs4 import BeautifulSoup
import requests

with open("/home/asher/leagueapi/champs/champs.json", "r") as r:
    champs = json.load(r)

url = "https://leagueoflegends.fandom.com"



temp = {}
c = "Kled"
temp[c] = champs[c]

champ_skins = {}
# for name,champ in list(champs.items())[:]:

for name,champ in temp.items():
    print(name)
    #print(url + champ["wiki-link"])
    htmldoc = requests.get(url + champ["wiki-link"]).content
    soup = BeautifulSoup(htmldoc, "html5lib")
    soup = soup.find("div",class_="mw-parser-output")
    
    #print(soup)
    soup = soup.find_all("div",class_="lazyimg-wrapper")[1]
    #print(len(soup))
    #print(soup)
    icons = soup.find_all("span",class_="skinviewer-show")
    
    splashes= soup.find_all("div",class_="skinviewer-tab-content")
    # print(len(icons))
    # print(len(splashes))
    skins = {}
    # print(len(icons))
    # print(len(splashes))
    if icons and splashes:
        print(len(icons))
        print(len(splashes))
        if len(icons) == len(splashes):
        
            for i,icon in enumerate(icons):
                splash = splashes[i]
                circle = icon.find("img")["data-src"]
                s = splash.find("a")["href"]
                n = icon.find("span",title=True)["title"]
                skins[n] = {}
                skins[n]["Splash"] = s 
                skins[n]["Icon"] = circle
                print(n)
    #print(skins)
    #print(skins)
    # champ_skins[name]["Skins"] = skins
    champs[name]["Skins"] = skins

with open("skintest.json", "w") as r:
    r.write(json.dumps(champs,indent=2))



    

    
