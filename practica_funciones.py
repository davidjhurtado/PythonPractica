# Practica de Funciones 
# Esta funciona Calcula Cuadrado es una función que recibe un número y lo multiplicar por él mismo
def CalculaCuadrado(numero):
   cuadrado = numero ** 2
   return cuadrado
# Mesaje es una funcion que devuelve un mensaje para el usuario
def Mensaje():
    return "Por favor escriba un número menor a 100: "

#########################################################
############# PROGRMA PRINCIPAL
########################################################

print("Programa para el Cálculo de Número cuadrados.")
nroinputinicial = int(input(Mensaje()))
nroinputfinal = int(input(Mensaje()))
if nroinputfinal < nroinputinicial:
    nrotemporal = nroinputfinal
    nroinputfinal = nroinputinicial
    nroinputinicial = nrotemporal
for number in range(nroinputinicial, nroinputfinal+1):
    print("Cuadrado de "+ str(number) + ": " + str(CalculaCuadrado(number)))
print("Fin")