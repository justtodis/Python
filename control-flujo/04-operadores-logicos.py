# operadores logicos = and, or, not

gas = True
encendido = True
edad = 18

if gas and encendido: # and necesita que las dos variables sean True para poder printearlo
    print("Puedes avanzar")

if gas or encendido: # or printeara si una variable es true da igual el resto
    print("Puedes avanzar")

if not gas or encendido: 
    print("Puedes avanzar")

if gas and (encendido or edad > 17): #aqui primero se ejecutara lo que hay dentro del parentesis
    print("Puedes avanzar")
