import dota2api
import urllib2
import os.path
import json



pwd = os.getcwd()
folder = pwd + '/hero_images'
if not os.path.exists(folder):
  os.makedirs(folder)



fo=open("steam_api_key.txt","r")
steam_api_key=fo.read()
fo.close()

fo=open("id_name.json","r")
id_name_dic=json.loads(fo.read())
fo.close()

api = dota2api.Initialise(steam_api_key)
heroes=api.get_heroes()["heroes"]
print("Downloading...")
i=0
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

for hero in heroes:
  if hero["localized_name"] != "Dawnbreaker":
    file_name=str(hero["id"])+" "+hero["localized_name"]+".png"
    req = urllib2.Request(hero["url_small_portrait"], headers=hdr)
    url_file = urllib2.urlopen(req)
    image_buffer = url_file.read()
    fo=open(folder+'/'+file_name,"wb")
    fo.write(image_buffer)
    fo.close()
    i = i + 1
print(i,"images were downloaded")

