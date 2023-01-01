import os
import wget
url = "https://github.com/cdufour/ingesys-unix-script/blob/main/python/tps/tp3/flags/flags.zip"
wget.download(url, 'C:/Users/A2M TRANSPORT/python/scripts/')

# creation du dossier flagsBis
try:
    os.mkdir("flagsBis")
    print("[+] dossier flagsBis a été créé")

except FileExistsError:
    print("erreur")
    exit(1)
    
try:
    os.mkdir("flags")
    print("[+] dossier flags a été créé")

except FileExistsError:
    print("erreur")
    exit(1)

import zipfile

from zipfile import ZipFile

with ZipFile('flags.zip', 'r') as zip_object:
    zip_object.extractall('flags')
    


for f in os.listdir("flags"):
        if f.endswith(".png") and f != 'missing.png':
            os.rename("flags/" + f,"flagsBis/" + f[0:2].upper() + ".png")
            print("[+] file %s moved" % f) 
