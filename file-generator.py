students = ["Augustin","Karim","Rawia","Alexandra"]

for s in students:

    #creation de nom de fichier
    filepath ="files/evaluation_" + s[:4].lower() + ".txt"
    print(filepath)

    f = open(filepath, "w")
    f = write.(content + s)
    f.close()