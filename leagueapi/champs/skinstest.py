import json



with open("/home/asher/leagueapi/champs/champs.json", "r") as r:
    champs = json.load(r)
with open("/home/asher/leagueapi/audio/audios.json", "r") as r:
    audios = json.load(r)

for name,champaudio in audios.items():
    skins = set()
    for quote,audio in champaudio.items():
        for skin in list(audio["Files"].keys()):
            #skins.add(skin)
            if skin not in champs[name]["Skins"].keys():

                # if(skin.replace(" ","")) in 
                # if skin.isalpha():
                skins.add(skin)
                    #print(quote)
                    #print(name,skin)
                
    if(not skins == set()):
        print(name,"\n\tAudio Files Skins:", skins)
                    
    #print(name,skins)

# THE FOLLOWING FIXES THE INCORRECT SKIN NAMES IN THE AUDIO FILE
# for name,champ in champs.items():
#     for skin in list(champ["Skins"].keys()):
#         for quote,audio in audios[name].items():
#             # if not skin in audio["Files"].keys() and skin.replace(" ", "") in audio["Files"].keys():
#             #     audio["Files"][skin] = audio["Files"][skin.replace(" ", "")]
#             #     audio["Files"].pop(skin.replace(" ",""))
#             #     print(skin)
#             # if name == "Dr. Mundo":
#             #     if not skin in audio["Files"].keys() and skin.replace(" Mundo","") in audio["Files"].keys():# and skinin audio["Files"].keys():
#             #         audio["Files"][skin] = audio["Files"][skin.replace(" Mundo", "")]
#             #         audio["Files"].pop(skin.replace(" Mundo",""))
#             #         print(name,skin)
            # if name == "Master Yi":
                # if not skin in audio["Files"].keys() and skin.replace(" Yi","") in audio["Files"].keys():# and skinin audio["Files"].keys():
                #     audio["Files"][skin] = audio["Files"][skin.replace(" Yi", "")]
                #     audio["Files"].pop(skin.replace(" Yi",""))
                #     print(name,skin)
            # if name == "Lux":
            #     bad = ['Dark', 'Mystic', 'Ice', 'Water', 'Air', 'Magma', 'Storm', 'Nature', 'Fire']
            #     BAD = False
            #     for b in bad:
            #         if b in audio["Files"].keys():
            #             BAD = True
            #             break
            #     if(BAD):
            #         print(quote)
                # if not skin in audio["Files"].keys() and BAD:# and skinin audio["Files"].keys():
                #     audio["Files"]["Elementalist"] = audio["Files"][skin.replace(" Yi", "")]
                #     audio["Files"].pop(skin.replace(" Yi",""))
                #     print(name,skin)
                
#             # if name == "Master Yi":
#             #     if not skin in audio["Files"]
#             if not skin in audio["Files"].keys() and skin.replace(" ", "") in audio["Files"].keys():
#                 audio["Files"][skin] = audio["Files"][skin.replace(" ", "")]
#                 audio["Files"].pop(skin.replace(" ",""))
#                 print(skin)


# # for name,champ in champs.items():
# #     for skin in champ["Skins"].values():
# #         for link in skin.values():
# #             if not link.startswith("https"):
# #                 print(link)

# with open("testaudio.json", "w") as r:
#     r.write(json.dumps(audios,indent=2))