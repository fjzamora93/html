from sys import argv
import sys



def hola():
    
    if len(argv)<2:
        nombre= input("¿Cómo te llamas? ")
    
    elif len(argv)>=2:
        nombre= argv[1]

    print (f"""¡Hola, {nombre}! Bienvenid@ a la calculadora de Javi, donde puedes: 
    \n SUMAR (+) \n RESTAR (-) \n MULTIPLICAR (*) \n DIVIDIR (/) \n POTENCIA (^) \n PORCENTAJE (%) \n 
    Tenemos dos modos de calculadora. \n """)

    seleccion= input("""¿Con qué calculadora te gustaría trabajar?\n
                    1. CALCULADORA CLÁSICA\n
                    2. CALCULADORA GATUNA\n""")
    
    if "gat" in seleccion or "2" in seleccion:
        calculadora_gatuna()
    elif "cl" in seleccion.lower() or "1" in seleccion:
        calculadora()



def calculadora():
    list_operador=["+", "-", "*", "/", "%", "^"]
    while True:
        try: 
            x= float(input ("x: "))
            operador= input ("¿Qué operación vas a realizar? (+, -, *, /, %, ^): ")
            while operador not in list_operador:
                print ("operador no válido! ")
                operador= input ("¿Qué operación vas a realizar? (+, -, *, /, %, ^): ")
            y= float(input ("y: "))
            break
        except ValueError:
            miau()
        except KeyboardInterrupt:
            print (f"\n ¡Nos vemos!" )
            sys.exit()
            


    while True:
        try:
            if operador.lower() == "+" or "sum" in operador.lower(): 
                resultado= suma (x,y) 
            elif operador == "-" or "rest" in operador.lower(): 
                resultado= resta (x,y) 
            elif operador == "*" or "mult" in operador.lower(): 
                resultado= multiplicacion (x,y) 
            elif operador == "/" or "div" in operador and y!=0: 
                resultado= division (x,y)
            elif operador == "^" or "pot" in operador or "elev" in operador:
                resultado= potencia (x,y)  
            elif operador == "%" or "porc" in operador:
                resultado= porcentaje (x,y)
            else:
                print("¡Algo salió mal! Prueba de nuevo: (+, -, *, /, %, ^)")

            print (f"resultado: {resultado}")
            operador= input ("Operación: ")
            while operador not in list_operador:
                print ("operador no válido! ")
                operador= input ("¿Qué operación vas a realizar? (+, -, *, /, %, ^): ")
            x=resultado
            y= float(input ("y: "))
        
        except KeyboardInterrupt:
            print ("\nAdiós!")
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


def calculadora_gatuna():
    print ("\n¡Miau! Estás en la calculadora Gatuna :3 ")
    while True:
        try: 
            x= int(input ("¿Cuántos gatos tienes?: "))
            operador= input ("¿Qué quieres hacer con los gatos? (+, -, *, /, %, ^): ")
            y= int(input ("¿Cuántas veces sucede? "))
            break

        except ValueError:
            print ("Parece que un gato pasó por encima de tu teclado... inténtalo de nuevo!")
            break
        except KeyboardInterrupt:
            print (f"\n ¡Nos vemos!" )
            sys.exit()

    try:

        if operador.lower() == "+" or "sum" in operador.lower(): 
            resultado= suma(x,y)
            print (f"    Si tienes {x} gatitos y adoptas {y} gatitos... tienes ¡{resultado}! gatitos") 
        elif operador == "-" or "rest" in operador.lower(): 
            resultado= resta (x,y)
            print (f"    ¡Oh no! Si tienes {x} gatitos y {y} gatitos se despeñan por la ventana... tienes ¡{resultado}! gatitos") 
        elif operador == "*" or "mult" in operador.lower(): 
            resultado= multiplicacion (x,y) 
            print (f"     Si tienes {x} gatas y cada gata tiene {y} gatitos... tienes ¡{resultado} gatitos recién nacidos! ")
        elif operador == "/" or "div" in operador and y!=0: 
            z=0
            decremento=x
            while decremento>=y:
                z += 1
                decremento -= y               
            resto= x-(z*y)
            
            print (f"    Al repartir tus gattitos, cada amigo tiene ¡{z} gatitos! y te sobran {resto} gatitos para ti!! ")




        elif operador == "^" or "pot" in operador or "elev" in operador:
            maullido= potencia (x,y)
            for _ in range (maullido):
                print ("        miau")
            print ("    ¡¡¡EXPLOSIÓN DE GATITOS!!!") 
        elif operador == "%" or "porc" in operador:
            resultado= porcentaje (x,y)*100
            print (f"    Tu gato es un {resultado}% adorable <3 <3 <3 <3 <3 <3!!!")
        else:
            print ("    Parece que un gato pasó por encima de tu teclado... inténtalo de nuevo!")
        
    except KeyboardInterrupt:
        print ("\nHay un gato sobre tu teclado!!! Ahora no puedes irte!!!")
        pass
    except ValueError:
        print ("El gato se ha descontrolado.. PfaepoFJPOFJMoijmdpoñedj!")
    except UnboundLocalError:
        print ("... dfanÑMK VF`PKZFACV`D E49dñ!... QUITA YA, pesado!!!")
    
    calculadora_gatuna()

       

def miau():
    print("    RESET")
    calculadora()


if __name__== "__main__": 
    hola()
