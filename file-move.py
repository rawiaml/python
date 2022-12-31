import os

#os.mkdir("blabla")
#os.rmdir("blabla")

# try:
#     os.rmdir("blabla")
# except FileNotFoundError:
#     print("le dossier n'existe pas")

#print(os.listdir("files"))

for f in os.listdir("files"):
    if f.endswith(".log"):
        os.rename("files/" + f,"files/logs/" + f)
        print("[+] file %s moved" %f)
print("the end")