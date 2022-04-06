import random
IMAGENES_AHORCADO = [r'''

 +---+
 |   |
     |
     |
     |
     |
 =========''', r'''

  +---+
  |   |
  O   |
      |
      |
      |
 =========''', r'''

  +---+
  |   |
  O   |
  |   |
      |
      |
 =========''', r'''

  +---+
  |   |
  O   |
 /|   |
      |
      |
 =========''', r'''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
 =========''', r'''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
 =========''', r'''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
 =========''']
palabras = 'hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre sapo trucha pavo tortuga comadreja ballena lobo wombat cebra'.split()

def obtenerPalabraAlAzar(listaDePalabras):
    # Esta funcion devuelve una cadena al azar de la lista de cadenas pasada como argumento
    indiceDePalabras = random.randint(0, len(listaDePalabras) - 1)
    return listaDePalabras[indiceDePalabras]

def mostrarTablero(IMAGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta):
     print(IMAGENES_AHORCADO[len(letrasIncorrectas)])
     print()

     print('Letras incorrectas:', end=' ')
     for letra in letrasIncorrectas:
          print(letra, end=' ')
     print()

     espaciosVacios = '_'*len(palabraSecreta)

     for i in range(len(palabraSecreta)):#completar los espacios vacios con las letras adivinadas
          if palabraSecreta[i] in letrasCorrectas:
               espaciosVacios = espaciosVacios[:i] + palabraSecreta[i] + espaciosVacios[i+1:]

     for letra in espaciosVacios:#mostrar la palabra secreta con espacios entre cada letra
          print(letra, end=' ')
     print()

def obtenerIntento(letrasProbadas):
     #devuelve la letra ingresada por el jugador. Verifica que el jugador ha ingresado solo una letra y no otra cosa.
     while True:
          print('Adivina una letra')
          intento = input()
          intento = intento.lower()
          if len(intento) != 1:
               print('Por favor, introduce solo una letra')
          elif intento in letrasProbadas:
               print('Ya has probado esa letra. Intenta otra.')
          elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
               print('Por favor ingresa una LETRA.')
          else:
               return intento

def jugarDeNuevo():
     #esta funcion devuelve True di el jugador quiere volver a jugar, en caso contrario devuelve False.
     print('¿Quieres jugar de nuevo? (si o no)')
     return input().lower().startswith('s')


print('A H O R C A D O')
letrasIncorrectas = ''
letrasCorrectas = ''
palabraSecreta = obtenerPalabraAlAzar(palabras)
juegoTerminado = False

while True:
     mostrarTablero(IMAGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)

     #permite al jugador escribir una letra
     intento = obtenerIntento(letrasIncorrectas + letrasCorrectas)

     if intento in palabraSecreta:
          letrasCorrectas = letrasCorrectas + intento

          #verifica si el jugador ha ganado
          encontradoTodasLasLetras = True
          for i in range(len(palabraSecreta)):
               if palabraSecreta[i] not in letrasCorrectas:
                    encontradoTodasLasLetras = False
                    break
          if encontradoTodasLasLetras:
               print('¡Sí! ¡La palabra secreta es "' + palabraSecreta + '"! ¡Has ganado!')
               juegoTerminado = True
     else:
          letrasIncorrectas = letrasIncorrectas + intento

          #comprobar si el jugador ha agotado sus intentos y ha perdido
          if len(letrasIncorrectas) == len(IMAGENES_AHORCADO) - 1:
               mostrarTablero(IMAGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)
               print('¡Te has quedado sin intentos!\nDespués de ' + str(len(letrasIncorrectas)) + ' intentos fallidos y ' + str(len(letrasCorrectas)) + ' aciertos, la palabra era "' + palabraSecreta + '"')
               juegoTerminado = True

     #preguntar al jugador si quiere volver a jugar (pero solo si el juego ha terminado)
     if juegoTerminado:
          if jugarDeNuevo():
               letrasIncorrectas = ''
               letrasCorrectas = ''
               juegoTerminado = False
               palabraSecreta = obtenerPalabraAlAzar(palabras)
          else:
               break