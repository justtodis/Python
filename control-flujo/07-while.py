numero = 1
while numero < 100:  # mientras numero sea menor a 100
    print(numero)
    numero *= 2 # multiplicar numero 2 

comando = ""

while comando.lower != "salir": #mientras comando sea diferente a salir , lower hace que lo que escribas se haga minusc
    comando = input("$ ") # comando es igual a input (input del usuario)
    print(comando)

while True:  # esto sera un loop infinito y solo se parara usando salir como vemos abajo
    comando = input("$ ") 
    print(comando)
    if comando.lower() == "salir": # aqui todo lo que escribas lo leera como salir aunque pongas SALIR o SaLiR
        break