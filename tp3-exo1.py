#import os
# os.mkdir("flagsBis")

import wget
url = "https://github.com/cdufour/ingesys-unix-script/blob/main/python/tps/tp3/flags"
wget.download(url, 'C:/Users/A2M TRANSPORT/python/scripts/flagsBis')
"""
from zipfile import ZipFile 
  
# spécifiant le nom du fichier zips
file = "C:/Users/A2M TRANSPORT/python/scripts/flagsBis/flags.zip"
  
# ouvrir le fichier zip en mode lecture
with ZipFile(file, 'r') as zip: 
    # afficher tout le contenu du fichier zip
    zip.printdir() 
  
    # extraire tous les fichiers
    print('extraction...') 
    zip.extractall() 
    print('Terminé!')
""" 