#EJEMPLO 1: Imprimir algunos tipos de dato y saber que datos corresponden
print ("Hello, World!") #Imprimir algo
print (len("Hello, World"))
print(type(10.5)) #Nos dice el tipo de dato que es
print(str(10)) #Convierte el numero a un string
print(float(10)) #Convierte el numero a un decimal

input("Enter your full name please :)")  #Acceder información


#EJEMPLO 2: Guardar valores en cada una de las variables
first_name = "José Ángel"
last_name = "Madrigal Cervantes"
country = "México"
age = 18
is_married = False #Boolean
skills = ["Python", "Spanish", "Play Videogames", "Fast Learning"] #Array

person_info = {       #Diccionario
    "First Name" : "José Ángel",
    "Last Name" : "Madrigal Cervantes",
    "Country" : "México", 
    "Single" : "Yes, Im single",
    }

print('Hello',',', 'World','!') #Puede tomar más de 1 argumento usando comas 

#EJEMPLO 3: Esto hace que imprima el parametro que le estamos declarando
print("First Name: ", first_name)
print("First Name Lenght: ", len(first_name))
print("Last Name: ", last_name)
print("Last Name Lenght ", len(last_name))
print("Country", country)
print("Age: ", age)
print("Is Married?", is_married)
print("Skills", skills)
print("Person Information", person_info)

#EJEMPLO 4: Declarar multiples variables en una sola linea
first_name, last_name, country, age, is_married = "José Ángel", "Madrigal Cervantes", "Mexico", 18, False
print("First Name: ", first_name)
print("Last Name: ", last_name)
print("Country", country)
print("Age: ", age)
print("Is Married?", is_married)


#SUMARY
first_name = input("What is your name?")
age = input("How old are you?")
print("Your name is beautiful ", first_name)
print(age)