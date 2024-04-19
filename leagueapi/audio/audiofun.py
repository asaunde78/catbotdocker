import json

with open("audios.json", "r") as r:
    audios = json.load(r)

all_tags = set()
AT = []
s=0

# for name,audio in audios.items():
#     for val in audio.values():
#         if("Files" in val):
#             s += len(val["Files"])
#             #print(len(val["Files"]))

    # for line in audio.keys():
    #     if "My name is" in line:
    #         print(line, name)
    # for quote,line in audio.items():
    #     if not "Files" in line.keys():
    #         print(quote,name)

    # for line in audio.values():
    #     a = line["Tags"]
    #     for tag in a:
    #         all_tags.add(tag)
    #         AT.append(tag)
    # for quote,line in audio.items():
    #     # if "Drake" in line["Tags"]:
    #     #     print(quote, name)
    #     for tag in line["Tags"]:
    #         if "Killing " in tag:
    #             print(quote, "\n\t",name, "\n\t\t-",tag)
    #             pass
    # ban = False
    # for line in audio.values():
    #     if "Pick" in line["Tags"]:
    #         ban = True
    #         break
    # if(not ban):
    #     print(name)
    # for line in audio.values():
    #     new = []
    #     for tag in line["Tags"]:
    #         if tag:
    #             tag = tag.replace("  ", " ")
    #             tag = tag.strip()
    #             print(tag)
    #             new.append(tag)
    #         # else:
    #         #     line["Tags"].remove(None)
    #     line["Tags"] = new



#print(all_tags)
# tagcount = {}
# for tag in all_tags:
#     tagcount[tag] = AT.count(tag)
# tagcount = dict(sorted(tagcount.items(), key=lambda x:x[1],reverse=True))
# with open("tagcount.json","w") as r:
#     r.write(json.dumps(tagcount, indent=2))
# with open("test.json","w") as r:
#     r.write(json.dumps(audios, indent=2))


