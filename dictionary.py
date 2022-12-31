d = {}
print(type(d))  #dict

student1 = {
"age": 25,
"lname": "PASCAL",
"fname": "Blaise",
"isGoodLearner": True,
"grades": [17, 12, 19.5]

}

student2 = {
"age": 35,
"lname": "PAS",
"fname": "Bla",
"isGoodLearner": True,
"grades": [19, 1, 16]

}

student3 = {
"age": 30,
"lname": "P",
"fname": "Bl",
"isGoodLearner": True,
"grades": [17, 12, 19.5]

}

#affichage de la premiere note 
print(student1["grades"][0])

for k in student1:
   # print(k) affiche les cles 

    print(k, "=>", student1[k])

students = [student1, student2, student3]
print(students)