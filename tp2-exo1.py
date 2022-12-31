# def PGTtctaxe1():
# prixHT = float(input("Prix Hors Taxe? "))
# taux = float(input("Taux taxe? "))
# taxe = prixHT * taux
# prixTTC = prixHT + taxecode 
# print("==> Avec un prix HT de ", prixHT, " et un taux de ", taux, sep="")
# print("==> La taxe vaut ", taxe, " et le prix TTC vaut ", prixTTC, sep="")
# PGTtctaxe1()

prices = [14, 100, 30, 10, 8]


def montantTva(price, tva):
return price * tva


tva = float(input("saisir un taux de tva (ex: 20, ou 5.5) : "))
pricesTtc = [x + montantTva(x, tva) for x in prices]

print(pricesTtc)