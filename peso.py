#Input
Peso_en_Tierra = float(input("Intro el peso en kgs: "))

#Proceso - Calcular el peso en los distintos planetas, con dos decimales.
Peso_en_Luna = round(Peso_en_Tierra * 1.622 / 9.81 , 2)
Peso_en_Mercurio = round(Peso_en_Tierra * 3.7 / 9.81, 2)
Peso_en_Venus = round(Peso_en_Tierra * 8.87 / 9.81, 2)
Peso_en_Marte = round(Peso_en_Tierra * 3.711 / 9.81, 2)
Peso_en_Jupiter = round(Peso_en_Tierra * 24.79 / 9.81, 2)
Peso_en_Saturno = round(Peso_en_Tierra * 10.44 / 9.81, 2)
Peso_en_Urano = round(Peso_en_Tierra * 8.69 / 9.81, 2)
Peso_en_Neptuno = round(Peso_en_Tierra * 11.15 / 9.81, 2)


#Output
print("El peso en la Luna es de: " + str(Peso_en_Luna) + "kg.")
print("El peso en Mercurio es de: " + str(Peso_en_Mercurio) + "kg.")
print("El peso en Venus es de: " + str(Peso_en_Venus) + "kg.")
print("El peso en Marte es de: " + str(Peso_en_Marte) + "kg.")
print("El peso en Jupiter es de: " + str(Peso_en_Jupiter) + "kg.")
print("El peso en Saturno es de: " + str(Peso_en_Saturno) + "kg.")
print("El peso en Urano es de: " + str(Peso_en_Urano) + "kg.")
print("El peso en Neptuno es de: " + str(Peso_en_Neptuno) + "kg.")


print("mira si se subio")
