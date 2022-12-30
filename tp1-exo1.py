import random
#secret=8
secret= random.randint(0, 10)
# print("mon chiffre secret est", secret)

while True:
    answer = int(input("devine mon chiffre secret:"))

    if answer == secret:
        break
    elif answer > secret:
        print("mon chiffre est plus petit")
    else:

        print("mon chiffre est plus grand")
print("bravo! bonne reponse")
