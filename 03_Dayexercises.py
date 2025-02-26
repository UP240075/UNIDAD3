import math

#EJERCICIO 1
age = 18

#EJERCICIO 2
height = 1.78

#EJERCICIO 3
complex_Number = 1j

#EJERCICIO 4
triangle_base = float(input("What is the triangle base"))
triangle_height = float(input("What is the triangle height"))
triangle_area = triangle_base * triangle_height * 0.5
print("The area of the triangle is ", triangle_area)

#EJERCICIO 5
side_A = float(input("Put the side A of the traingle  "))
side_B = float(input("Put the side B of the triangle  "))
side_C = float(input("Put the side C of the triangle  "))
triangule_Perimeter = side_A + side_B + side_C
print("The perimeter of the triangle is  " , triangule_Perimeter)

#EJERCICIO 6
rectangleLength = float(input("Put the length of the ractangle"))
rectangleWidth = float(input("Put the width of the rectangle "))
area = rectangleLength * rectangleWidth
print("The area of ypur rectangle is  ", area)
rectanglePerimeter = (rectangleLength + rectangleWidth) * 2
print("The perimeter of your rectangle is " ,rectanglePerimeter)

#EJERCICIO 7
circle_Radius = float(input("Put the radius"))
circle_Area = math.pi * (circle_Radius**2)
circumference = 2 * math.pi * circle_Radius
print("The Area is   ", circle_Area)
print("The circumference is ",circumference )

#EJERCICIO 8
# z = 2q - 2    q = x z = y
q1, z1, q2,z2 = 1, 0, 0, -2
FirstSlope = (z2 - z1) / (q2  - q1)
print("The slope is    ", FirstSlope)

#EJERCICIO 9
x1,y1,x2,y2 = 2,2,6,10
Second_Slope = (y2 - y1) / (x2 - x1)
print("The slope is" , Second_Slope)
euclidean_Distance = math.sqrt((x2 - x1) **2 + (y2-y1) ** 2)
print("La distancia Eucladiana es  ", euclidean_Distance)

#EJERCICIO 10
if (FirstSlope == Second_Slope):
    print("It is the same")
else: print("It is not the same, YOU ARE WRONG!")

#EJERCICIO 11
print("Evaluando la función y = x^2 + 6x + 9")
for x in range(-10, 11):  # Prueba con valores de x entre -10 y 10
    y = x**2 + 6*x + 9
    print(f"x = {x} -> y = {y}")
    if y == 0:
        print(f"Encontrado: y es 0 cuando x = {x}")



#EJERCICIO 12
word1 = len("Python")
word2 = len("dragon")
if (word1 != word2):
    print("It is a diferent length")
else: "It is the same length"

#EJERCICIO 13
print('on' in 'python' and 'on' in 'dragon')  # Output: True


#EJERCICIO 14
print("jargon" in "I hope this course is not full of jargon")

#EJERCICIO 15
print("no" in "dragon" and "no" in "Python")

#EJERCICIO 16
pythonLen = len("Python")
print(float(pythonLen))
print(int(pythonLen))

#EJERCICIO 17
number = float(input("Put a number"))
reminder = number % 2
if (reminder == 0):
    print("The number is divisible for 2") 
else: print("The number is not divisible for 2")

#EJERCICIO 18
floorDivision = 7 / 3
if floorDivision == int(2.7):
    print("It is not equal   ")
else: print("It is equal   ")

#EJERCICIO 19
# Definir valores
a = '10'  # Cadena
b = 10    # Entero
# Comparar tipos
result = type(a) == type(b)
# Mostrar resultado
print("¿El tipo de '10' es igual al tipo de 10?:", result)

#EJERCICIO 20
if "9.8" == 10:
    print(True)
else: False

#EJERCICIO 21
hours = float(input("¿Cuántas horas trabajas?"))
perHour = float(input("¿Cuánto te pagan por hora?"))
weeklyEarning = hours * perHour
print("Tu salario es de $  ", weeklyEarning)

#EJERCICIO 22
while True:
    try:
        yearsLived = int(input("¿Cuántos años tienes? (entre 0 y 100): "))
        if 0 <= yearsLived <= 100:
            break
        else:
            print("Ingresa un número entre 0 y 100.")
    except ValueError:
        print("Error: Ingresa un número entero.")
secondsInYourLife = yearsLived * 3153600000 
print("Has vivido por", secondsInYourLife, "segundos")

#EJERCICIO 23
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)
