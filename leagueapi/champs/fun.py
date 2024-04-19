import json

with open("champs.json", "r") as f:
    champs = json.load(f)

# champs = champs["Champions"]
# aliases = {}
# for name in champs.keys():
#     aliases[name.lower()] = name
#     if("'" in name):
#         aliases[name.lower().replace("'","")] = name
#         print(name)
# with open("aliases.json","w") as r:
#     r.write(json.dumps(aliases, indent=2))


# for name, champ in champs["Champions"].items():
#     if "Related character(s)" not in champ["Info"].keys():
#         print(name)
# for name, champ in champs["Champions"].items():
#     for name_,champ_ in champs["Champions"].items():
#         if not name == name_:
#             set1 = set()
#             set2 = set()

#             for x in champ["Info"]["Related character(s)"]:
#                 set1.add(x)
#             for y in champ_["Info"]["Related character(s)"]:
#                 set2.add(y)
#             if(set1 == set2):
#                 print(name)
# m = 0
# MPC = ""
# for name, champ in champs["Champions"].items():
#     R = champ["Info"]["Related character(s)"]
#     if(type(R)==str):
#         current = 1
#     else:
#         current = len(R)
#     if(current > m):
#         m = current
#         MPC = name
# MPC = "Kindred"
# print(MPC,champs["Champions"][MPC]["Info"]["Related character(s)"])

# weapons = {}
# for name,champ in champs["Champions"].items():
#     weapons[name] = champ["Info"]["Weapon(s)"]
# print(weapons)
# with open("weapons.json", "w") as r:
#     r.write(json.dumps(weapons,indent=2))


    # if len(champ["Info"]["Related character(s)"]) == 2:
    #     print(name, champ["Info"]["Related character(s)"])
# for name,champ in champs["Champions"].items():
    # if(not "Status" in champ["Info"].keys()):
    #     print(name)
    # if "They" in champ["Info"]["Pronoun(s)"]:
    #     print(name + "\n\t" + (champ["Info"]["Pronoun(s)"]))
    
# infokeys = set()
# for name, champ in champs["Champions"].items():
#     keys = list(champ["Info"].keys())
#     for item in keys:
#         infokeys.add(item)
# #print(infokeys)
# c = {}
# for name,champ in champs["Champions"].items():
#     #key = name
#     #value = []
#     for key in infokeys:
#         if not key in champ["Info"].keys():
#             champ["Info"][key] = "None"
#     #c[name]=value
            
# with open("champs.json", "w") as r:
#     r.write(json.dumps(champs,indent=2))
