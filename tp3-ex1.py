import os
import wget

# télécharger le fichier "flags.zip"
url = "https://github.com/cdufour/ingesys-unix-script/blob/main/python/tps/tp3/flags/flags.zip"
wget.download(url, 'C:/Users/A2M TRANSPORT/python/scripts/')

# creation du dossier flagsBis
try:
    os.mkdir("flagsBis")
    print("[+] dossier flagsBis a été créé")

except FileExistsError:
    print("erreur")
    exit(1)
# créattion du dossie flags  
try:
    os.mkdir("flags")
    print("[+] dossier flags a été créé")

except FileExistsError:
    print("erreur")
    exit(1)

# extraction du fichier flags.zip dans le dossier "flags"
import zipfile

from zipfile import ZipFile

with ZipFile('flags.zip', 'r') as zip_object:
    zip_object.extractall('flags')

# deplacer les fichiers de flags vers flagBis en les renomant  
    
for f in os.listdir("flags"): 
    if f.endswith(".png") and f != 'missing.png':
        os.rename("flags/" + f,"flagsBis/" + f[0:2].upper() + ".png")
        print("[+] file %s moved" % f) 
