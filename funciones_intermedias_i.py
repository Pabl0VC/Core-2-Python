#--------------------------1.Actualizar valores en diccionarios y listas--------------------------------

from re import X
from tkinter import N

#1. Cambia el valor 10 en x a 15
x = [ [5,2,3], [10,8,9] ] 

print(x) # Salida: [[5, 2, 3], [10, 8, 9]]
valorCambio = x[1][0]
print(valorCambio) # Salida: 10
x[1][0] = 15
print(x) # Salida: [[5, 2, 3], [15, 8, 9]] 



#2. Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

print(estudiantes [0]) #salida: {'first_name': 'Michael', 'last_name': 'Jordan'}
print(estudiantes[0]['last_name']) # Salida: Jordan
estudiantes[0]['last_name'] = 'Bryant'
print(estudiantes[0]['last_name']) # Salida: Bryant
print(estudiantes [0]) #Salida: {'first_name': 'Michael', 'last_name': 'Bryant'}



#3.En el directorio_deportes, cambia "Messi" por "Andrés".
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}

print(directorio_deportes['fútbol'][0]) #Salida: Messi
directorio_deportes['fútbol'][0] = 'Andrés'
print(directorio_deportes['fútbol'][0]) #Salida: Andrés
print(directorio_deportes) #Salida: {'basketball': ['Kobe', 'Jordan', 'James', 'Curry'], 'fútbol': ['Andrés', 'Ronaldo', 'Rooney']}



#4. Cambia el valor 20 en z a 30.
z = [ {'x': 10, 'y': 20} ]

print(z[0]['y']) #Salida: 20
z[0]['y'] =  30
print(z) #Salida: [{'x': 10, 'y': 30}]


#---------------------------------2.Iterar a través de una lista de diccionarios--------------------------------

estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


def iterateDictionary(x):
    for i in x:
        deportista = ' ' #bonus
        for key in i:
            deportista += key + ' - ' + i[key] + ','
        print(deportista)

iterateDictionary(estudiantes)

#-------------------------3.Obtener valores de una lista de diccionarios-----------------------------------

estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan',},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


def nameDictionary(k,x):
    for i in x:
        print(i[k])
nameDictionary('first_name',estudiantes)
nameDictionary('last_name',estudiantes)




# ----------------------4. Iterar a través de un diccionarios con valores de lista--------------------------
dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(x):
    print(len(x['ubicaciones']), 'ubicaciones'.upper())
    for ubicacion in x['ubicaciones']:
        print (ubicacion)
    print('')
    print(len(x['instructores']), 'instructores'.upper())
    for instructor in x['instructores']:
        print (instructor)

printInfo(dojo)






