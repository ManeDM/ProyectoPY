#El programa genera la sucesión de Fibonacci hasta el valor numero indicado
numero=int(input("Enter the value of 'n': "))
#Los dos primeros terminos son primero y segundo
primero=0
segundo=1
suma=0
cuenta=1
print("Fibonacci Sequence: ")
# Cuenta no puede ser mayor a numero
while(cuenta<=numero):    
  cuenta+=1
  primero=segundo
  segundo=suma
  suma=primero+segundo	
  print(suma)
