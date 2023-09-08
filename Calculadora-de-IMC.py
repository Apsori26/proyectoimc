# Ya que nos piden que:
# El programa no puede permitir que ningún dato quede vacío,
# Cree la siguiente variable para poder realizar las validaciones
personas = input('Escribe la cantidad de personas a evaluar en numero: ')
contador = len(personas)
indice = 0
#acontinuacion para poder evalual la cantidad de personas a las cuales se les solicitaran sus datos
#realizamos un while a la cual la variable contador se le estara disminuyendo una unidad cada que termine el proceso
#por persona.
while(0 < contador): 
    natural = 0
    bandera = False
    #aqui realizamos la validacion para que el dato que ingresen sea un numero y de esa manera nuestro programa
    #no colapse, en caso que el usuario ingresa otro dato diferente, le solicitara que lo ingrese de nuevo.
    while(natural < 10):
        if(personas [indice] == str(natural)):
             bandera = True
             break
        natural = natural + 1   
    contador = contador - 1
    indice = indice + 1
    if(bandera == False):
        print('los datos ingresados no son correctos ')
        personas = input('Escribe la cantidad de personas a evaluar en numero: ')
        contador = len(personas)
        indice = 0
personas = int(personas)

while(0 < personas):
    vacio = ''
    # validamos que se ingrese un nombre
    nombre = input('Escribe tu nombre: ')
    while(nombre == vacio ):
        nombre = input('Escribe tu nombre: ')
    # validamos que se ingrese un apellido paterno
    apellido_paterno= input('Escribe tu apellido paterno: ')
    while(apellido_paterno == vacio):
        apellido_paterno = input('Escribe tu apellido paterno: ')
    # validamos que se ingrese un apellido materno
    apellido_materno = input('Escribe tu apellido materno: ')
    while(apellido_materno == vacio):
        apellido_materno = input('Escribe tu apellido paterno: ')

    # validamos que se ingrese una edad de tipo entero

    edad = input('Escribe tu edad en años: ')
    contador = len(edad)
    indice = 0
    while(0 < contador):
        natural = 0
        bandera = False
        while(natural < 10):
            if(edad [indice] == str(natural)):
                bandera = True
                break
            natural = natural + 1   
        contador = contador - 1
        indice = indice + 1
        if(bandera == False):
            edad = input('Escribe tu edad en años: ')
            contador = len(edad)
            indice = 0
    # edad = int(edad)
    # validamos que se ingrese una masa de tipo flotante

    peso = input('Escribe tu peso en kg: ')
    contador = len(peso)
    indice = 0
    while(0 < contador):
        natural = 0
        bandera = False
        while(natural < 10):
            if(peso [indice] == str(natural) or peso [indice] == '.'):
                bandera = True
                break
            natural = natural + 1   
        contador = contador - 1
        indice = indice + 1
        if(bandera == False):
            peso = input('Escribe tu peso en kg: ')
            contador = len(peso)
            indice = 0
    peso = float(peso)

    # validamos que se ingrese una altura de tipo flotante

    estatura = input('Escribe tu estatura en metros: ')
    contador = len(estatura)
    indice = 0
    while(0 < contador):
        natural = 0
        bandera = False
        while(natural < 10):
            if(estatura [indice] == str(natural) or estatura [indice] == '.'):
                bandera = True
                break
            natural = natural + 1   
        contador = contador - 1
        indice = indice + 1
        if(bandera == False):
            estatura = input('Escribe tu estatura en metros: ')
            contador = len(estatura)
            indice = 0
    estatura = float(estatura)

    # calculamos su IMC con la siguiente formula

    masa = peso / estatura**2 
    # imprimimos en pantalla todos los datos de la persona
    # junto a su masa corporar que se obtubo

    print('Tu nombre es: ' + nombre.title())
    print('Tu apellido paterno es: ' + apellido_paterno.title())
    print('Tu apellido materno es: ' + apellido_materno.title())
    print('Tu edad es: ' + edad)
    if(int(edad) < 18):
        print('eres menor de edad')
    else:
        print('eres mayor de edad')
    print('Tu peso es: ' + str(peso))
    print('Tu estatura es: ' + str(estatura))
    print(f'Tu indice de masa corporal es: {masa:.2f}')

    IMC = masa
    #determinamos en que estado se encuentra con respecto a su masa corporal
    print('Lo cual indica que presentas un estado: ')
    if (IMC >= 0 and IMC <= 15.99):
            print ("De delgadez severa")
    else:
        if (IMC >= 16.00 and IMC <= 16.99) :
            print ("De delgadez moderada")
        else:
            if (IMC >= 17.00 and IMC <= 18.49):
                print ("De delgadez leve")
            else:
                if (IMC >= 18.50 and IMC <= 24.99) :
                    print ("Normal")
                else:
                    if (IMC >= 25.00 and IMC <= 29.99):
                        print ("De sobrepeso")
                    else:
                        if (IMC >= 30.00 and IMC <= 34.99):
                            print ("De obesidad leve")
                        else:
                            if (IMC >= 35.00 and IMC <= 39.00):
                             print ("De obesidad media")
                            else:
                                if (IMC >= 40.00):
                                    print ("De obesidad morbida")
    personas = personas -1

