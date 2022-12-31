
f= open("files/demo.txt", "r")
#print(type(f))
content = f.read()
f.close()

newcontent = content.replace("demo","preuve")
print(content)
print(newcontent)

f2= open("files/new", "w") # creation du deuxieme fichier 
f2.write(newcontent)
f2.close()