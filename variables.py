#variables primitives en python
temperature = 2
pi = 3.14
isEarthRound = True
training = "initiation au langage python"
#affichage de type des variables
print(type(temperature))
print(type(pi))
print(type(isEarthRound))
print(type(training))


# print(2+2)

# print(temperature + temperature)
# training = "perfectionnement au langage python"
# print(training)

# operation sur les variables
print(temperature + 10)
print( training + "10") #concatenation entre 2 chaines
print(pi + 10) # addition float et entier
print(isEarthRound + 10) #conversion implicite true=>1
print("le double de pi est:" + str(pi * 2)) # fonction de conversion str()

doublepi = pi * 2 # stockage en variable du retour d'une expression arith
print(type (doublepi))
doublepistr = str(doublepi)
print(type(doublepistr))
