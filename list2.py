

posteCodes = [
    67200, 75012, 15000, 75020,
    67200, 75012, 15000, 75020,
    67275, 75012, 15000, 75020,
    75007, 75012, 15000, 75020
]

#combien de codes postaux parisiens?
# variable d'accum
# parcourir la liste
#recherche tt ce qui commence par 75
# increment accu quand parisien  est trouvé

numParis = 0
for posteCode in posteCodes:
    if posteCode >= 75000 and posteCode <= 75999:
        numParis += 1
print("nombre de codes postaux", numParis)

#autre exemple de "slicing"
# affichage des 3 deniers code de la liste initial 

print(posteCodes[0:3])
print(posteCodes[-3:])

for p in posteCodes[-3:]:
    print(p)
