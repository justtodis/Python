n1 = input("Ingresa primer numero") # Input es la funcion para que el usuario inserte un numero o texto
n2 = input("Ingresa segundo numero")

n1 = int(n1) # int es la funcion que almacena un valor numerico no decimal
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multi = n1 * n2
div = n1 / n2

mensaje = f"""Para los numeros {n1} y {n2}
el resultado de la suma es {suma}
el resultado de la resta es {resta}
el resultado de la multiplicación es {multi}
el resultado de la división es {div}.
"""
# La f antes del string es para poner variables dentro del string

print(mensaje)