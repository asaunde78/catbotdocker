import json
from moviepy.editor import AudioFileClip, ImageClip, CompositeVideoClip, TextClip
import pathlib
import requests
import random

from threading import Thread

with open("/home/asher/leagueapi/champs/champs.json", "r") as r:
    champs = json.load(r)
with open("/home/asher/leagueapi/audio/audios.json", "r") as r:
    audios = json.load(r)

import os, shutil
folder = 'contents/'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))
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

def generate(c = None, skin=None, tags = None, quote = None):
    res = search(champ=c,skin=skin,tags=tags,quote=quote)
    if len(list(res)) == 0:
        return
    print("Results: ", len(list(res)))

    name = random.choice(list(res.keys()))
    champdata = res[name]

    quote = random.choice(list(champdata.keys()))
    quotedata = champdata[quote]


    #print(quote,quotedata)
    if skin:
        link = quotedata["Files"][skin]
        skinname = skin
    else:
        skinname = random.choice(list(quotedata["Files"].keys()))
        link = quotedata["Files"][skinname]
    #print(skinname)
    print(quote,skinname)
    file_name = f"{quote}" +".ogg"
    # link = audios[champ][quote]["Files"]["Original"]
    print("Skin: ", skinname)
    pic = champs[name]["Skins"][skinname]["Splash"]
    #print(pic)
    pic_file = f"{name}" + ".jpg"


    with requests.get(link, allow_redirects=True) as response, open("contents/" + file_name, 'wb') as f:
        #print(response.text)
        data = response.content
        f.write(data)
    with requests.get(pic,allow_redirects=True) as response, open("contents/" + pic_file, "wb") as f:
        data = response.content
        f.write(data)
    audio_clip = AudioFileClip("contents/" + file_name)
    image_clip = ImageClip("contents/" + pic_file)

    video_clip = image_clip.set_audio(audio_clip)
    video_clip.duration = audio_clip.duration
    video_clip.fps = 1
    # txt_clip = TextClip(quote+"\n-"+name,stroke_width=2,stroke_color="black",method="caption",color="white",size=(1215,200),font="Roboto")
    txt_clip = TextClip(quote+"\n-"+name,stroke_width=2,stroke_color="black",method="caption",color="white",size=(1215,250),font="Roboto")


    txt_clip = txt_clip.set_pos(("center","bottom")).set_duration(audio_clip.duration)
    video_clip = CompositeVideoClip([video_clip, txt_clip])
    video_clip.duration = audio_clip.duration
    video_clip.write_videofile("contents/" + f"{name}"+".mp4")

    pathlib.Path("contents/" + file_name).unlink(missing_ok=True)
    pathlib.Path("contents/" + pic_file).unlink(missing_ok=True)
    #return "contents/" +f"{name}"+".mp4"

    #pathlib.Path("contents/" +f"{name}"+".mp4").unlink(missing_ok=True)





used = []
[Thread(target=generate(skin="Original")).start() for x in range(1)]


