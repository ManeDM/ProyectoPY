def puntuacion(clase):
    return sum(clase) / len(clase) 

clase = [7, 8, 9]
media = puntuacion(clase)
print("La puntuacion de esta clase es", media)

clase = [5, 7, 9.5, 4.2]
media = puntuacion(clase)
print("La puntuacion de esta clase es", media)


