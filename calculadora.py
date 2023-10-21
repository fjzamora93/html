
import sys


print ("Bienvenido a la Calculadora de Javi, donde puedes \n SUMAR (+) \n RESTAR (-) \n MULTIPLICAR (*) \n DIVIDIR (/) \n POTENCIA (^) \n PORCENTAJE (%) \n Pero de momento comencemos introduciendo el valor de X ")

def calculadora():


    while True:
        try: 
            x= int(input ("x: "))
            operador= input ("introduzca un operador válido (+, -, *, /, %, ^): ")
            y= int(input ("y: "))
            break
        except ValueError:
            miau()


    while True:
        try:
            if operador.lower() == "+" or "suma" in operador.lower(): 
                resultado= suma (x,y) 
            elif operador == "-": 
                resultado= resta (x,y) 
            elif operador == "*": 
                resultado= multiplicacion (x,y) 
            elif operador == "/" and y!=0: 
                resultado= division (x,y)
            elif operador == "^":
                resultado= potencia (x,y)  
            elif operador == "%":
                resultado= porcentaje (x,y)
            else:
                print("¡Algo salió mal! Prueba de nuevo: (+, -, *, /, %, ^)")

            print (f"resultado: {resultado}")
            operador= input ("introduzca un operador válido (+, -, *, /, %, ^): ")
            x=resultado
            y= int(input ("y: "))
        
        except KeyboardInterrupt:
            print ("Adiós!")
            break
        except ValueError:
            miau()
        except UnboundLocalError:
            miau()


def suma (x,y):
    return x+y
def resta (x,y):
    return x-y
def multiplicacion (x,y):
    return x*y
def division (x,y):
    return x/y
def porcentaje (x,y):
    return x*y/100
def potencia (x,y):
    if y < 0:
        x = 1 / x
        y = -y
    resultado = 1
    
    for _ in range(y):
        resultado *= x
    return resultado


def miau():
    print("    RESET")
    calculadora()

calculadora()
    print("    ¿Qué has tocado ya? Empecemos de nuevo...")
    calculadora()

calculadora()

