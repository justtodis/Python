nombre_curso = "Ultimate Python" #string es una cadena de texto
descripcion_curso = """
Ultimate Python,
este curso comtempla todos los detalles que necesitas
para encontrar trabajo 
como programador
""" # triple comillas para strings con texto largo
print(nombre_curso, descripcion_curso) # para nombrar varias variables
print(len(nombre_curso)) # para printear el numero de letras que tiene la variable nombre_curso
print(nombre_curso[0]) # para printear la primera letra se empieza desde cero
print(nombre_curso[0:8]) # para printear desde la primera hasta la octava letra
print(nombre_curso[9:]) # printeara desde la letra 9
print(nombre_curso[:9]) # printeara lo anterior a la letra 9
print(nombre_curso[:]) # si no ponemos nada sera el texto entero