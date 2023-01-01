import os
# os.mkdir("flagsBis")
import glob
"""
import subprocess
ziploc = "C:/Program Files/7-Zip/7z.exe" #location where 7zip is installed
cmd = [ziploc, 'e', "flags.zip" ,'-o'+ "C:/Users/A2M TRANSPORT/python/scripts/flagsBis",'-r' ] 
#sp = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)

import wget
url = "https://github.com/cdufour/ingesys-unix-script/blob/main/python/tps/tp3/flags/flags.zip"
wget.download(url, 'C:/Users/A2M TRANSPORT/python/scripts/flagsBis')
"""
# from zipfile import ZipFile 
# # spécifiant le nom du fichier zip
# file = "archive.zip"
  
# # ouvrir le fichier zip en mode lecture
# with ZipFile(file, 'r') as zip: 
#     # afficher tout le contenu du fichier zip
#     zip.printdir() 
  
#     # extraire tous les fichiers
#     print('extraction...') 
#     zip.extractall() 
#     print('Terminé!')

# from urllib import request
# # fichier distant à récupérer
# url = 'https://github.com/cdufour/ingesys-unix-script/blob/main/python/tps/tp3/flags/allemagne.png'
# # le nom du fichier local 
# fichier = 'C:/Users/A2M TRANSPORT/python/scripts/flagsBis/allemagne.png'
# # Telecharger & enregistrer
# request.urlretrieve(url,fichier)

# import zipfile
         
# zip = zipfile.ZipFile('C:/Users/A2M TRANSPORT/python/scripts/flagsBis/flags(1).zip')
# zip.extract('*.png', 'C:/Users/A2M TRANSPORT/python/scripts/flagsBis/')
 
# zip.close()

import zipfile

from zipfile import ZipFile
# url = "C:\\Users\\A2M TRANSPORT\\python\\scripts\\flagsBis\\flags (1).zip"
with ZipFile('flags (1).zip', 'r') as zip_object:
    zip_object.extractall()
    
    