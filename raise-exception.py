#raise Exception("blabla")


def check(x):
    if x < 0:
        #print("négatif")
        raise Exception("negative number forbidden")

try:

    check(-4)
except:
    print("preblem")
    
print("***the end")