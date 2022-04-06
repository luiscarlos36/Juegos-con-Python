#Este es el juego de adivinar el número
import random

intentosRealizados = 0

print('¡Hola! ¿Cómo te llamas?')
miNombre = input()

numero = random.randint(1, 20)
print('Bueno ' + miNombre + ', estoy pensando en un número entre el 1 y el 20')

while intentosRealizados < 6:
    print('Intenta adivinar')
    estimacion = input()
    try:
        estimacion = int(estimacion)
    except:
        print('Ingresa un número puñetas')
        continue

    if estimacion < 0 or estimacion > 20:
        print('No se pase de verga compa, no esté jugando. Ingrese un numero entre 0 y 20')
        continue
    intentosRealizados += 1

    if estimacion < numero:
        print('Tu estimación es muy baja')
    
    elif estimacion > numero:
        print('Tu estimacion es muy alta')
    
    elif estimacion == numero:
        break

if estimacion == numero:
    intentosRealizados = str(intentosRealizados)
    print('¡Buen trabajo ' + miNombre + '! Has adivinado mi numero en ' + intentosRealizados + ' intentos.')
    
if estimacion != numero:
    numero = str(numero)
    print('Pues no. El numero que estaba pensando era ' + numero)
