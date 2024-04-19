import json 
from bs4 import BeautifulSoup
import requests

with open("/home/asher/leagueapi/champs/champs.json", "r") as r:
    champs = json.load(r)

url = "https://leagueoflegends.fandom.com"

def gena(name, champ_audio, audiolines, Skin = "Original"):
    # champ_audio = {}
    # champ_audio[name] = {}
    #audiolines = soup.find_all(["h2","dl","ul","h3"])
    
    #print([tag.name for tag in audiolines])
    for index,tag in enumerate(audiolines):
        #print(index)
        if(tag.name=="ul"):
            order = ["dl","h3","h2"]
            i = index - 1
            tags = []
            while len(order) >0 and i >= 0:
                #print(audiolines[i].name)
                if (audiolines[i].name in order):
                    #print(order)
                    order = order[order.index(audiolines[i].name)+1:]
                    #print(f"popped {audiolines[i].name}!")
                    #print(audiolines[i].name)
                    tappend = audiolines[i].text
                    #print(tappend)
                    #print(tappend)
                    if(audiolines[i].name == "dl"):
                        #print(audiolines[i].dt.string)
                        tappend = audiolines[i].find("dt")
                        if(tappend):
                            tappend = tappend.text
                        elif(tappend):
                            tappend = audiolines[i].i.text
                    
                    if(tappend):
                        tappend = tappend.replace("  ", " ")
                        tappend = tappend.strip()
                    #print(tappend)
                    tags.append(tappend)
                i -= 1
            audios = tag.find_all("li")
            #print(tags)
            texts = []
            # if Skin == "Spirit Blossom":
            #     print(audios[0])
            for audio in audios:
                
                files = audio.find_all("div",class_="audio-button")
                skins = audio.find_all("span",class_="skin-play-button")
                
                if files:
                    files = [f.find("audio")["src"] for f in files]
                if skins:
                    skins = [skin["data-skin"] for skin in skins]

                a = audio.find('i')
                if a and files:
                    quote = a.text
                    if len(skins) == 0:
                        skins = [Skin]#["Original"]
                    #print(quote)
                    
                    if quote in champ_audio[name]:
                        start = 1
                        #print(quote)
                        #print(quote+(str(start)))
                        while quote + " " + str(start) in champ_audio[name].keys():
                            start += 1
                            #print("added")
                        quote = quote + " " + str(start)
                    champ_audio[name][quote] = {}

                    skinlink = {}
                    #print(f"Skins: {len(skins)} Files: {len(files)}")
                    while len(skins) < len(files):
                        skins.append( Skin + " "+ str(len(skins) + 1))
                    if(len(skins)==len(files)):
                        for jndex, skin in enumerate(skins):
                            skinlink[skin] = files[jndex]
                        champ_audio[name][quote]["Files"] = skinlink
                    #print(skinlink)
                    # if skinlink == {}:
                    #     print(quote)
                    #champ_audio[name][quote]["audio-skins"] = skins

                    texts.append(quote)
            tags = [t for t in tags if not t is None]
            if not texts == []:
                for t in texts:
                    champ_audio[name][t]["Tags"] = tags
                #print(tags, texts)
    #print(champ_audio)
            



temp = {}
c = "Lux"
temp[c] = champs[c]

champ_audio = {}
# for name,champ in list(champs.items())[:]:
for name,champ in temp.items():
    champ_audio[name] = {}
    print(name)
    if(not name == "Nunu & Willump"):
        audiolink= url + champ["wiki-link"]+"/Audio####"
    else:
        audiolink = url + "/wiki/Nunu/LoL/Audio####"
    htmldoc = requests.get(audiolink).content
    soup = BeautifulSoup(htmldoc, "html5lib")
    soup = soup.find("div",class_="mw-parser-output")
    #possibleskins = soup.find("ul", class_=)
    classic = soup.children
    classic = [tag for tag in classic if tag.name in ["h2","dl","ul","h3"]]
    gena(name,champ_audio,classic)

    potentialskins = soup.find_all("div",class_="wds-tabs__tab-label")
    if potentialskins:
        print([skin.text for skin in potentialskins])
    else: 
        # d = gena(name, "Original", soup.find_all(["h2","dl","ul","h3"]))
        # for k,v in d.items():
        #     champ_audio[k] = v
        print("no tabs just one")
        gena(name,champ_audio,soup.find_all(["h2","dl","ul","h3"]))
        #print("????????")
    
    skintabs = soup.find_all("div",class_="wds-tab__content")
    #print(len(skintabs))
    if(skintabs and len(skintabs) == len(potentialskins)):
        for index,tab in enumerate(skintabs):
            
            skinname = potentialskins[index].a.string
            print(skinname)
            if skinname == "Spirit Blossom":
                #print(tab.text)
                pass
            if skinname.string == "Classic":
                skinname = "Original"
            # d = gena(name, skinname, tab.find_all(["h2","dl","ul","h3"]))
            # for k,v in d.items():
            #     champ_audio[k] = v
            gena(name, champ_audio, tab.find_all(["h2","dl","ul","h3"]),Skin=skinname)



            
with open("test.json", "w") as r:
    r.write(json.dumps(champ_audio, indent=2))
            


        # if(tag.name in ["h2","h3","dl"]):
        #     i = index + 1
        #     if tag.name == "h2":
        #         pass
        #         #print(tag.text.strip())
        #     elif tag.name == "h3":
        #         pass
        #         #print("\t" + tag.text.strip())
        #     elif tag.name == "dl":
        #         pass
        #         #print("\t\t", tag.text.strip())
        #     title = tag.text
        #     subtitle = None
        #     if i<len(audiolines)-1 and audiolines[i].name in ["h2","h3","dl"]:
        #         print("case")
        #         subtitle = audiolines[i].text
        #         i += 1
                

        #     while i < len(audiolines)-2 and not audiolines[i].name in ["h2","h3"] :
        #         #print(tag.text)
        #         nxt = (audiolines[i])
        #         if nxt.name == "ul":
        #             print(f"\t\t\tMain Values index:{i} Title:{title}" + (f" Subtitle: {subtitle}" if subtitle else "") )
        #             #print(f"\t\t\tMain Values index:{i}")
        #         i += 1
        
    # with open(name+"test.txt", "w") as r:
    #     r.write(soup.prettify())
# with open("audios.json", "w") as r:
#     r.write()

