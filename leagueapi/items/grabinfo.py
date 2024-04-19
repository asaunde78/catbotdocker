import requests 
from bs4 import BeautifulSoup
import json
import re

with open("items.json", "r") as r:
    items = json.load(r)

for i,item in list(items["Items"].items())[:]:
    if(item["Type"]=="Distributed items"):
        continue
    print(i)
    url = "https://leagueoflegends.fandom.com" + item["wiki-link"]
    r = requests.get(url).content
    soup = BeautifulSoup(r,"html5lib")
    
    box = soup.find("aside", role="region", class_="portable-infobox")
    sections = box.find_all("section")

    image = box.find("img")
    if(image):
        item["icon"] = image["src"]
    #print(image["src"])

    item_info = {}
    for section in sections:
        
        #print(section.text)
        
        fields = section.find_all("div",class_="pi-item")
        if fields:
            key = ""
            key = section.find("h2")
            if(key):
                key = key.text
            #print(key)
            value = []
            
            for field in fields:
                #print(title)
                # answers = field.find_all("a")
                # if(answers):
                #     #value = [answer.text for answer in answers if  not answer.text == ""]
                #     print("\t" + str([answer.text for answer in answers if  not answer.text == ""]))
                answers = field.find_all("li")
                if(answers):
                    value = [answer.text for answer in answers if not answer.text == ""]
                    #print("\t" + str([answer.text for answer in answers if not answer.text == ""]))
                    
                answer = field.find("div")
                if(answer and not key == "Menu"):
                    #value = answer.text
                    #print("\t" + answer.text)
                    value.append(answer.text)
        else:
            recipe= section.find("tr")
            costs = section.find("td",{"data-source":"buy"})

            availability=section.find_all("tr")

            
            #print(costs)
            key = None
            value = []

            if(recipe):
                recipe_items = recipe.find_all("a")
                #costs = recipe.find("tbody")
                #print(costs)
                if(recipe_items):
                    #print("Build Path")
                    key = "Build Path"
                    # print(recipe_items[0]["title"])
                    value = [item_["title"] for item_ in recipe_items]
                    # for val in value:
                    #     if "Gold" in val:
                    #         val = item["href"]  
            if(costs):
                #print("Cost")
                key = "Cost"
                if(costs.find("a")):
                    value = costs.find("a")["title"]
                #print(costs)
            elif(availability and len(availability)>1):
          
                a = availability[0]
                b = availability[1]
                #print("Availability")
                key = "Availability"
                #print(len(availability))
                value = []
                value = {td["data-source"].upper():td.find("img")["title"] for td in b.find_all("td")}
                # print([ m.text for m in a.find_all("span")])
                # print([title["title"] for title in b.find_all("img")])
                    
    
        if(key):
            #print({key:value})
            item_info[key] = value
    #print(item_info)
    item["Info"] = item_info

with open("temp.json","w") as r:
    r.write(json.dumps(items, indent=2))
    #print(name)


            
            
                
