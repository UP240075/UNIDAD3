#EJERCICIO 1
W1, W2, W3, W4 = "Thirty", "Days", "Of", "Python"
CompleteSentence = W1 + " " + W2 + " " + W3 + " "+ W4 + "."
print(CompleteSentence)

#EJERCICIO 2
WW, WW2, WWW3, Zpace = "Coding" , "For" , "All", "  "
print(WW + Zpace + WW2 + Zpace + WWW3 )

#EJERCICIO 3
company = "Coding For All"

#EJERCICIO 4
print (company)

#EJERCICIO 5
print(len(company))

#EJERCICIO 6
text = "Company"
uppercase_text = text.upper() #La función .upper hace todos los caracteres mayusculas
print(uppercase_text)

#EJERCICIO 7
print (text.lower())  #La función .lower hacr todos los caracteres minusculas

#EJERCICIO 8
stringWord = "Coding For All"
print(stringWord.capitalize())
print(stringWord.title())
print(stringWord.swapcase())

#EJERCICIO 9
texto = "Coding For All"
replacetextointenso = texto.replace("Coding","" )
print(replacetextointenso)

#EJERCICIO 10
codingforall = "Coding For All"
if codingforall.find("Coding") == 0:  # Devuelve la posición de "Coding"
    print(True)
else:
    print(False)

#EJERCICIO 11
replaceWord = codingforall.replace("Coding" , "Python")
print(replaceWord)

#EJERCICIO 12
moreReplaceWord = replaceWord.replace("Python", "Everyone").replace("All", "Python")
print(moreReplaceWord)

#EJERCICIO 13
splitText = codingforall.split()
print(splitText)
#Esto hace que genere una lista espaciada
#Existen diferentes párametros que pueden ponerse en el .split()
#Algunos parametros son split.(separador, maxsplit , "," , " ", )

#EJERCICIO 14
empresas = "Facebook, Google, Microsoft, Apple, IBM, ORacle, Amazon"
splitEmpresas = empresas.split(",")
print(splitEmpresas)

#EJERCICIO 15
forAll = "Coding For All"
onlyOne = forAll[0]
print(onlyOne)

#EJERCICIO 16
lastOne = forAll[-1] #Al ser un index negativom empieza desde atras
print(lastOne)

#EJERCICIO 17
idexten = forAll[10]
print(idexten)

#EJERCICIo 18
textoo = "Python For Everyone"
acronym = "".join(word[0] for word in textoo.split())
print(acronym)

#EJERCICIO 19
mastexto = "Coding For All"  #Declaras la variable de tu texto
masacronimos = "".join(word[0] for word in mastexto.split()) 
print(masacronimos)

#EJERCICIO 20
eltexto = "Coding For All"
position = eltexto.index("C")
print(position)

#EJERCICIO 21
position2 = eltexto.index("F")
print(position2)

#EJERCICIO 22
eltesto = "Coding For All"
encontrareltesto = eltesto.find("l")
print(encontrareltesto)

#EJERCICIO 23
text = "You cannot end a sentence with because because because is a conjunction"
posicion = text.find("because") 
print(posicion)

#EJERCICIO 24
text = "You cannot end a sentence with because because because is a conjunction"
anotherposition = text.rindex("because")-1
print(anotherposition)

#EJERCICIO 25
textocortado = "You cannot end a sentence with because because because is a conjunction"
#Lo reemplazara por un espacio vacío
textoepico = textocortado.replace("because because because", "")
print(textoepico)

#EJERCICIO 26
text = "You cannot end a sentence with because because because is a conjunction"
posicion = text.find("because") 
print(posicion)

#EJERCICIO 27
textocortado = "You cannot end a sentence with because because because is a conjunction"
textoepico = textocortado.replace("because because because", "")
print(textoepico)
 
#EJERCICIO 28
substring = "Coding For All"
if substring.find("Coding") == 0:
    print(True)
else: print(False)

#EJERCICIO 29
substring = "Coding For All"
if substring.find("coding") == 11:
    print(True)
else: print(False)

#EJERCICIO 30
removeSpaces = "   Coding For All   "
removidosJeje = removeSpaces.replace("   ", "")
print(removidosJeje)

#EJERCICIO 31
var1 = '30DaysOfPython'
print(var1.isidentifier()) # Falso
var2 = 'thirty_days_of_python'
print(var2.isidentifier()) # Verdadero
# La función isidentifier checa si puede o no ser un nombre valido para crear una variable

#EJERCICIO 32
librerias = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
# Unir la lista con "# " como separador
result = " # ".join(librerias)
print(result)

#EJERCICIO 33
separar = "I am enjoying this challenge.\nI just wonder what is next."
print(separar)
#La función \n hace un espacio en diferentes lineas

#EJERCICIO 34
tabular = "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print(tabular)
#La función \t sirve para que tabule las palabras y esten alineadas correctamente

#EJERCICIO 35
radius = 10
area = 3.14 * radius ** 2
# Formateando con f-string
formatear = f"The area of a circle with radius {radius} is {area} meters square."
print(formatear)
#La letra f hace que toda la cadena siguiente se haga un string
#{} todo dentro de la llave sera visto como una expresión

#EJERCICIO 36
masformateointenso = f"Las operaciones aritmeticas de 8 y 6 son su suma de {8+6},\n su resta es {8-6}, la multiplicación de \n{8*6}, su division de {8%6}, su {8//6} y su potencia de {8**6} "
print(masformateointenso)