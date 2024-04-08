animal = " CHanchito Feliz "
print(animal.upper()) # lo que hace upper es coger variable animal y lo pone en mayusculas
print(animal.lower()) # lo que hace upper es coger variable animal y lo pone en minuscula
print(animal.capitalize()) # lo que hace es poner en mayusc primera letra del string y resto en minusc
print(animal.title()) # lo que hace es poner cada primera letra de cada palabra en mayusc y resto en minusc
print(animal.strip()) # lo que hace es elimitar los espacios a izq y derech del spring
print(animal.lstrip()) # quitaria los espacios de la izquierda
print(animal.rstrip()) # quitaria los espacios de la derecha
print(animal.strip().capitalize()) # asi se encadenarian varios strings
print(animal.find("CH")) # lo que hace es buscar la primera letra de lo que busquemos por ejemplo de CH es C
print(animal.find("cH")) # nos printeara -1 porque la c minuscula no la encontró
print(animal.replace("CH", "J")) # cambiara CH por J
print("CH" in animal) # busca si la variable tiene CH y pondra true or false
print("CH" not in animal) # busca si la variable NO tiene CH y pondra true or false