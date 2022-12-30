

#liste de 3 entiens 
numbers = [23, 140, 0]
print(type(numbers)) 

for n in numbers:
    print(n)

title ="les trois mousq"
print(title[4])

for c in title:
    print(c)

acc = 0 #variable accumulateur
search = "s"

for c in title:
    if c == search:
        acc= acc + 1
print("le caractere %s a été trouvé %d fois" % (search, acc))
