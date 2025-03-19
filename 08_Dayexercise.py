#Un Dictionary es una colección desordenada y modificable

#EJERCICIO 1
dog = {}

#EJERCICIO 2
dog = {
    "Name" : "Ramon",
    "Color" : "Blanco",
    "Breed" : True,
    "Legs" : 4,
    "Age" : 3
}

#EJERCICIO 3
student_dictionary = {
    "First Name" : "José Ángel",
    "Last Name" : "Madrigal Cervantes",
    "Gender" : "Masculino",
    "Age" : 18,
    "Martial Status" : "Single",
    "Skills" : ["Python", "Leer", "Jugar videojuegos", "Japonés"],
    "Country" : "México",
    "City" : "Aguascalientes", 
    "Adress"  : "Que te importa"
}

#EJERCICIO 4
print(len(student_dictionary))

#EJERCICIO 5
valor_habilidades = student_dictionary["Skills"]
print(valor_habilidades)  
print(type(valor_habilidades))  

#EJERCICIO 6

student_dictionary["Skills"].append("Godot")
student_dictionary["Skills"].append("SolidWorks")
print(student_dictionary)

#EJERCICIO 7
values = student_dictionary.values()
print(values)

#EJERCICIO 8 
values_list = list(student_dictionary.values())
print(values_list)

#EJERCICIO 9
print(student_dictionary.items())

#EJERCICIO 10
student_dictionary.pop("Age")
print(student_dictionary)

#EJERCICIO 11
del student_dictionary