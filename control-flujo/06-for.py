for numero in range(5): # for le daria el valor que dice range y range dice 5.            RANGE(5) ES UN ITERABLE
    print(numero) # por lo cual se printearia numero que seria 0,1,2,3,4

for numero in range(5):
    print(numero, numero * "hola mundo") # aqui printearia numero (0,1,2..) y numero (5 veces) hola mundo

buscar = 3
for numero in range(5): 
    print(numero)
    if numero == buscar:
        print("encontrado", buscar) 
        break #break es para detener el script. En este caso porque el numero 3 ha sido encontrado

buscar = 10
for numero in range(5): 
    print(numero)
    if numero == buscar:
        print("encontrado", buscar) 
        break 
else: # este else es que si despues del break al no encontrar el numero entonces...
    print("no encontre el numero")



for ejemplo in "Ultimate python":  # tambien con un string. El valor de ejemplo pasaria a ser "Ultimate python"
    print(ejemplo)

