def primo(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True            

def calculadora():
    num = int(input("Ingresa un numero:"))
    result = primo(num)

    if result is True:
        print('El numero es primo!!')
    else:
        print('El numero no es primo!!')

if __name__ == '__main__':
    calculadora()

    

    print("felicitaciones amigo, aprendiste a subir cambios y actualziaciones a tu repositorio, un commit")