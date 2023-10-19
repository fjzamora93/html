
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
            if operador == "+": 
                resultado= x+y 
            elif operador == "-": 
                resultado= x-y 
            elif operador == "*": 
                resultado= x*y 
            elif operador == "/" and y!=0: 
                resultado= x/y 
                

            elif operador == "^":
                resultado= x
                if y<0:       
                    for _ in range (-y-1): 
                        resultado=(x*resultado)
                    resultado= 1/resultado
                else:   
                    for _ in range (y-1):
                        resultado=x*resultado
                
            elif operador == "%":
                resultado= x*y/100

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


def miau():
    print("    ¿Qué has tocado ya? Empecemos de nuevo...")
    calculadora()

calculadora()

