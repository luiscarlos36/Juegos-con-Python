import turtle
import time
import random

posponer = 0.1

#Marcador
score = 0
high_score = 0

# Configuracion de la ventana
wn = turtle.Screen()
wn.title('Juego de Snake')
wn.bgcolor('black')
wn.setup(width = 600, height = 600)
wn.tracer(0)

# Cabeza de la serpiente
cabeza = turtle.Turtle() # Crea el objeto
cabeza.speed(0) # Para que cuando iniciemos, la figura ya esté ahí
cabeza.shape('square') # Forma de la figura
cabeza.color('white')
cabeza.penup() # El objeto no deja ningún rastro
cabeza.goto(0, 0)
cabeza.direction = 'stop'

#Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape('circle')
comida.color('red')
comida.penup()
comida.goto(0, 100)

# Segmentos / Cuerpo de la serpiente
segmentos = []

#Texto
texto = turtle.Turtle()
texto.speed(0)
texto.color('white')
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write('Score: 0       High Score: 0', align = 'center', font = ('Courier', 24, 'normal'))

# Funciones
def arriba():
    cabeza.direction = 'up'
def abajo():
    cabeza.direction = 'down'
def izquierda():
    cabeza.direction = 'left'
def derecha():
    cabeza.direction = 'right'

def mov():
    if cabeza.direction == 'up':
        y = cabeza.ycor()
        cabeza.sety(y + 20)
    if cabeza.direction == 'down':
        y = cabeza.ycor()
        cabeza.sety(y - 20)
    if cabeza.direction == 'left':
        x = cabeza.xcor()
        cabeza.setx(x - 20)
    if cabeza.direction == 'right':
        x = cabeza.xcor()
        cabeza.setx(x + 20)

# Teclado
wn.listen()
wn.onkeypress(arriba, 'Up')
wn.onkeypress(abajo, 'Down')
wn.onkeypress(izquierda, 'Left')
wn.onkeypress(derecha, 'Right')

while True:
    wn.update()

    #Colisiones con los bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0, 0)
        cabeza.direction = 'stop'

        #Esconder los segmentos
        for segmento in segmentos:
            segmento.goto(2000, 2000)

        #limpiar lista de segmentos
        segmentos.clear()

        #Resetear marcador
        score = 0
        texto.clear()
        texto.write('Score: {}       High Score: {}'.format(score, high_score), align = 'center', font = ('Courier', 24, 'normal'))

    if cabeza.distance(comida) < 20: #Porque por defecto los objetos tienen tamaño de 20 x 20 pixeles. Si la distancia entre ellos es esa, significa que se han tocado.
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape('square')
        nuevo_segmento.color('grey')
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

        #Aumentar marcador
        score += 10

        if score > high_score:
            high_score = score
        
        texto.clear()
        texto.write('Score: {}       High Score: {}'.format(score, high_score), align = 'center', font = ('Courier', 24, 'normal'))

    #Mover el cuerpo de la serpiente
    totalSeg = len(segmentos)
    for index in range(totalSeg - 1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x, y)

    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x, y)

    mov()

    #Colisiones con el cuerpo
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0, 0)
            cabeza.direction = 'stop'

            #Esconder los segmentos
            for segmento in segmentos:
                segmento.goto(1000, 1000)

            #Limpiar los elementos de la lista
            segmentos.clear()

            #Resetear marcador
            score = 0
            texto.clear()
            texto.write('Score: {}       High Score: {}'.format(score, high_score), align = 'center', font = ('Courier', 24, 'normal'))
    time.sleep(posponer)