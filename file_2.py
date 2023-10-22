
"""
En la clase anterior veíamos cómo trabajar con un documento de txt.

En esta ocasión, vamos a ver de qué manera se relacionan los datos entre sí.
Para ello, vamos a abrir un documento de csv.

"""

with open ("tabla.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",") 
            #Lo primero es separar cada item de la tabla con la coma
            #Pero lo más llamativo es que hemos creado DOS VARIABLES a la vez.
            
        print (f"{name[0]} is in {house[1]}")

#MINUTO 40
