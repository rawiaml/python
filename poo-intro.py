class Student:
    #propriétés
    age = 0
    first_name = ""
    last_name = ""
    
    # propriété privé 
    __age = 0
    
    # definition de la fonction test
    def test(self):
        print("test")
    # accesseur (getter)
    def get_age(self):
        return self.__age
    
    def get_first_name(self)
        return self.first_name
    
    #mutateurs (setters)
    def set_age(self, age)
        self.__age
# instanciation 
s1 = Student()
s2 = Student()
#print(type(s1))
s1.first_name = "Toto"
print(s1.first_name)
print(s2.first_name)

# invocation d'une méthode à partir d'un objet

s1.test()
s2.test()

# print (s1.__age)
s1.set_age(99)
print(s1.get_age())

print(s1.get_first_name())