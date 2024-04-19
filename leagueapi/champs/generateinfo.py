import requests

from bs4 import BeautifulSoup
import json

with open("champs.json", "r") as f:
    champs = json.load(f)

for c in list(champs["Champions"].values())[:]:#[champs["Champions"]["Corki"]]:#
    link = c["wiki-link"].replace("/LoL","")
    url = "https://leagueoflegends.fandom.com" + link
    print(url)
    htmldoc = requests.get(url).content
    soup = BeautifulSoup(htmldoc, "html5lib")
    block = soup.find_all("aside",role="region",class_="portable-infobox")[1]
    pictype =  block.find("div", class_="pi-image-collection")
    if pictype:
        renders = pictype.find_all("div",class_="wds-tab__content")
        pics = [render.a["href"] for render in renders]
    else:
        
        #print("One pic")
        pics = [block.find("figure",class_="pi-item").a["href"]]
        #print(pics)

    
    current_renders = c["champ-render"]
    if(not type(current_renders) == list):
        current_renders = [current_renders]
    for pic in pics:
        if not pic in current_renders: 
            current_renders.append(pic)
    c["champ-render"] = current_renders

    sections = block.find_all("section")
    character_info = {}
    for section in sections:
        
        #print(section.text)
        if "Related character" in section.text:
            #print(section)
            key = ""
            value = ""
            key = section.find("h2").text
            related = section.find("nav").find_all("a")

            value = [ch.text for ch in related]
            value = [ch for ch in value if not ch == ""]

            if len(value)==1:
                value = value[0]
            character_info[key] = value
            print(character_info)
        # else:
        #     fields = section.find_all("div",class_="pi-item")
        #     for field in fields:
        #         key = ""
        #         key = field.find("h3").text
        #         value = ""
        #         #print(title)
        #         answers = field.find_all("a")
        #         if(answers):
        #             value = [answer.text for answer in answers if  not answer.text == ""]
        #             #print("\t" + str([answer.text for answer in answers if  not answer.text == ""]))
        #         else:
        #             answer = field.find("div")
        #             if(answer):
        #                 value = answer.text
                
        #         answers = field.find_all("li")
        #         if(answers):
        #             value = [answer.text for answer in answers if not answer.text == ""]
        #             #print("\t" + str([answer.text for answer in answers if not answer.text == ""]))
                    

                
                
                    
        #             #print("\t" + answer.text)
        #         if len(value)==1:
        #             value = value[0]
        #         character_info[key] = value
    # with open("temp.json", "w") as r:
    #     r.write(json.dumps(character_info, indent=2))
    for key,value in character_info.items():
        c["Info"][key]=value 
    #print(character_info)
    #print(c)

with open("champs.json","w") as r:
    r.write(json.dumps(champs,indent=2))
# with open("champs.json","w") as r:
#     r.write(json.dumps(champs,indent=2))
