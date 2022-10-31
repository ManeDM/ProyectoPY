print("Inicio")
print("Bienvenido a la isla. Tu misión será encontrar el tesoro.")
print("¿Quieres Avanzar?")
decision = input()
if(decision == "si"):
    print("Avanzas por un camino que si bifurca") 
    print("¿Que direccion quieres tomar izquierda o derecha?")
    
    camino = input()
    if(camino == "izquierda"):
        print("ves muy poco, avanzas un buen rato sosteniendote de las paredes")
        print("Das con una cueva cálida, hay agua cristalina y frutos, también encuentras un mensaje en un muro que dice *los temores de tus ojos y corazón el tereso te entregaran*")
        print("usas este sitio para descansar unas cuantas horas")
        print("Continuas con el camino hasta que te encuentras con una laguna subterránea dentro de la cueva")
        print("Puedes seguir tu camino, al final de este vez un brillo intenso, tambien te fijas que la laguna tiene un pequeño pasadizo sumergido")
        print("puedes nadar o seguir con tu camino ¿que haces? escribe A para nadar o B para seguir con el camino que llevas")
        nado = input()
        if(nado == "A"):
            print("En realidad el pasillo es corto y da a una cámara bastante maltratada por el tiempo")
            print("Te encuentras con unos escombros y unas pequeñas estatuillas, nada especiales y de aspecto deteriorado")
            print("son estatuas realmente deterioradas ¿quisieras tomarlas?")
            estatuila = input()
            if(estatuila =="si"):    
                print("Al ver que las estatuillas estaban bastante deterioradas, muy frustrado decides azotar una de ellas fuertemente contra el piso")
                print("Ves que de su interior resplandece una geam brillate y perfectamente redonde, rompes todas las otras 50 estatuas en el lugar y continuas por un pasillo que tiene pastante luz")
                print("Sales de la cueva, justo al lado opuesto de la isla, en tus manos llevas todo el botin. ")
                print("Congratulation ¡you WIN")
            else:
                print("Continuas por un pasillo que tiene bastante luz, parece natural")
                print("Sales de la cueva, sin posibilidad de volver a entrar, todo el esfuerzo fue para nada")
        else:
            print("Caminas para darte cuenta que llegas  a una cámara con unas bellísimas piedras que brillan en la oscuridad")
            print("Súbitamente vomitas sangre y te das cuenta que las piedras son radioactivas y mueres")
            print("GAME - OVER")

    else:
        print("Avanzas por un angosto pasillo, para rapido descubrir  ruidos que provienen de otro aventurero haciendo una fogata")
        print("notas que no se ha percatado de tu presencia ¿sigues de largo o llamas su atencion? Escribe A para seguir tu camino o escribe B para llamar su atencion")
                
        percepcion = input()
        if (percepcion == "B"):
            print ("La otra persona al notarte se pone en guardia y te dispara una flecha directo al corazón, caes muerto ")
            print ("GAME OVER")
        else:
            print("Continuas con tu camino")
            print("Das con una cueva cálida, hay agua cristalina y frutos, también encuentras un mensaje en un muro que dice *los temores de tus ojos y corazón el tereso te entregaran*")
            print("Usas este sitio para descansar hasta el siguiente día. ")
            print("Continuas con el camino hasta que te encuentras con una laguna subterránea dentro de la cueva")
            print("Puedes seguir tu camino, al final de este vez un brillo intenso, tambien te fijas que la laguna tiene un pequeño pasadizo sumergido")
            print("puedes nadar o seguir con tu camino ¿que haces? escribe A para nadar o B para seguir con el camino que llevas")
        nado = input()
        if(nado == "A"):
            print("En realidad el pasillo es corto y da a una cámara bastante maltratada por el tiempo")
            print("Te encuentras con unos escombros y unas pequeñas estatuillas, nada especiales y de aspecto deteriorado")
            print("son estatuas realmente deterioradas ¿quisieras tomarlas?")
            estatuila = input()
            if(estatuila =="si"):    
                print("Al ver que las estatuillas estaban bastante deterioradas, muy frustrado decides azotar una de ellas fuertemente contra el piso")
                print("Ves que de su interior resplandece una geam brillate y perfectamente redonde, rompes todas las otras 50 estatuas en el lugar y continuas por un pasillo que tiene pastante luz")
                print("Sales de la cueva, justo al lado opuesto de la isla, en tus manos llevas todo el botin. ")
                print("Congratulation ¡you WIN")
            else:
                print("Continuas por un pasillo que tiene bastante luz, parece natural")
                print("Sales de la cueva, sin posibilidad de volver a entrar, todo el esfuerzo fue para nada")
        else:
            print("Caminas para darte cuenta que llegas  a una cámara con unas bellísimas piedras que brillan en la oscuridad")
            print("Súbitamente vomitas sangre y te das cuenta que las piedras son radioactivas y mueres")
            print("GAME - OVER")  

else:
    print("Mueres por falta de recursos")
    print("Mueres - GAME OVER")