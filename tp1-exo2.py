n = int(input("Tapez la valeur de n "))

if n < 0 or n > 1000:
    print("le nombre doit etre compris entre 0 et 1000")
    exit()
else:
    print("La table de multiplication de : ", n," est :")

for i in range(0,11):
    print(i , " x ", n, " = ",i*n)