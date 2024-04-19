import json

with open("audios.json","r") as r:
    audios = json.load(r)


def search(champ: str = None,tags: list =None,quote:str=None,skin:str=None):
    result = {}
    # if(champ):
    #     return {champ:audios[champ]}
    for name,champaudio in audios.items():
        result[name] = {}
        #print(name)
        if(champ):
            if not name == champ:
                continue
        for linequote,data in champaudio.items():
            if(quote):
                #print("hi")
                if quote not in linequote:
                    continue
            if(tags):
                skip = False
                for tag in tags:
                    if tag not in " ".join(data["Tags"]):
                        #print(tag)
                        skip = True
                        break
                if skip:
                    continue
                        
            if(skin):
                #print("hi")
                if skin not in data["Files"]:
                    continue
            #print(linequote)
            #print(data["Tags"])
            result[name][linequote] = data
        #print(result[name] if not name == "Aatrox" else "FART")
    for name,r in list(result.items()):
        if r == {}:
            #print("hello?")
            result.pop(name)
    return result

# res = search(quote="Where",tags=["Joke"])
res = search(quote = "Mr. Root")

with open("searchoutput.json", "w") as r:
    r.write(json.dumps(res,indent=2))