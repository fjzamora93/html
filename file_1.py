"""
En esta clase vamos a aprender a guardar variables en archivos independientes.

Hasta ahora, una forma de guardar las variables era en listas a través del método "append".

"""

#Primera forma de append:
names=[]
for _ in range (1):
    name=input ("¿Cómo te llamas? ")
    names.append(name)

#Segunda forma de append:
nombres=[]
for _ in range (1):
    nombres.append(input("¿Tu nombre? "))

"""
El problema de esta forma de guardar información es que 
se inicia el programa. Así que para evitarlo, hay que crear un archivo donde se almacene.
"""

flor=input ("Nombre de flor: ")

file= open("flores.txt", "a") #Esto nos dice que vamos a abrir este documento.
                                #Escribimos una "a" de "append"
                                #Si escribimos una "w" (write), todo se borraría cada vez que empezásemos.
                                #Si escribimos "r" es "read mode"
file.write(f"{flor}\n") #Aquí estamos diciendo lo que vamos a escribir (la variable)
file.close() #No es estrictamente necesario cerrar el archivo... pero es una buena práctica.

"""
Aunque técnicamente esta no es la única forma de crear un archivo.
Podemos crear el archivo de otra forma que nos permita mantenerlo abierto
y seguir escribiendo código sin miedo a que se corrompa:

"""

animal= input ("Animal: ")

with open ("animal.txt", "a") as file:
    file.write (f"{animal}\n")

#MODO LECTURA
 
with open ("animal.txt", "r") as file:
    lines= file.readlines() #Con el modo lectura necesitamos guardar el file en una variable.

for line in lines:
    print ("Hola, ", line.rstrip()) 
    #Y a continuación imprimimos cada variable
    #Simplemente por diseño, aplicamos el .rstrip para quitar el doble enter.

"""
Aquí podemos simplificar un poco más el código todavía:
Lo que haremos será crear el bucle dentro del propio archivo.
Así no será necesario crear una variable independiente.


bestiario=[]
with open ("animal.txt") as file:
    for line in file:
        bestiario.append(line.rstrip)

for bestia in sorted(bestiario):
    print (f"Esto es {bestia}")



Pero en este momento esto no nos interesa... ya que vamos
a ir un paso más lejos y vamos a guardar el contenido
del documento txt en una lista.
"""
with open ("animal.txt", "r") as file:
    for line in sorted(file): #Cuidado! El sorted tiene en cuenta las mayúsculas.
        print ("Holi, holi! ", line.rstrip())


#Averiguar por qué esta línea de código está mal.
