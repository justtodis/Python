edad = 66
if edad > 65: # si la edad es superior a 65 
    print ("Puede ver la pelicula con super-descuento") # se printeara esto
if not edad > 65: # si la edad no es superior a 65
    print ("Hola")
elif  edad > 54:
    print("Puedes ver la pelicula con descuento")
elif edad > 17:
    print("Puedes ver la pelicula")    
else: #en caso de que la edad no es superior a 17
    print("No puedes entrar") # se printeara esto

print ("Listo")


# if siempre va antes de elif. elif es como una pregunta secundaria. 
# en el ejemplo el if pregunta por la edad del descuento
# entonces no preguntara la de la mayoria de edad


