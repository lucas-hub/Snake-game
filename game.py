# Snake Game #

import turtle
import time
import random

delay = 0.1

pontos = 0
pontuacao_maxima = 0

# Implementando tela do jogo
window = turtle.Screen()
window.title('Snake Game')
window.bgcolor('lightgreen')
window.setup(width=600, height=600)
window.tracer(0)

# Implementando a "comida" da cobra
comida = turtle.Turtle()
comida.speed(0)
comida.shape('square')
comida.color('blue')
comida.penup()
comida.goto(0, 100)

# Implementando a cobra
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('white')
head.penup()
head.goto(0, 0)
head.direction = 'stop'

# Criando um "caneta" com o módulo turtle
caneta = turtle.Turtle()
caneta.speed(0)
caneta.shape('square')
caneta.color('white')
caneta.penup()
caneta.hideturtle()
caneta.goto(0, 260)
caneta.write('Pontuação:0 ---- Pontuação máxima:0',
             align='center', font=('Courier', 20, 'normal'))

# Funções
segmento = []


def movimento():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)


def pra_cima():
    if head.direction != 'down':
        head.direction = 'up'


def pra_baixo():
    if head.direction != 'up':
        head.direction = 'down'


def pra_esquerda():
    if head.direction != 'right':
        head.direction = 'left'


def pra_direita():
    if head.direction != 'left':
        head.direction = 'right'


# Keyboard Bindings
window.listen()
window.onkeypress(pra_cima, 'Up')
window.onkeypress(pra_baixo, 'Down')
window.onkeypress(pra_esquerda, 'Left')
window.onkeypress(pra_direita, 'Right')

# Loop infinito para atualizar os frames da tela
while True:
    window.update()

    # Checa a colisão com as bordas
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(0.5)
        head.goto(0, 0)
        head.direction = 'stop'

        # Desaparece com as partes do corpo coletadas anteriormente quando o jogo reseta
        for partes in segmento:
            partes.goto(1000, 1000)

        segmento.clear()

        # Reseta a pontuação
        pontos = 0

        # Reseta a velocidade
        delay = 0.1

        caneta.clear()
        caneta.write('Pontuação:{} ---- Pontuação máxima:{}'.format(pontos,
                                                                    pontuacao_maxima), align='center', font=('Courier', 20, 'normal'))

    # Checa a colisão entre a cobra e a comida
    if head.distance(comida) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        comida.goto(x, y)

    # Adiciona um segmento no corpo
        novo_segmento = turtle.Turtle()
        novo_segmento.speed(0)
        novo_segmento.shape('square')
        novo_segmento.color('black')
        novo_segmento.penup()
        segmento.append(novo_segmento)

        # Adiciona pontos
        pontos += 10

        # Aumenta a velocidade do jogo
        delay -= 0.002

    if pontos > pontuacao_maxima:
        pontuacao_maxima = pontos

    caneta.clear()
    caneta.write('Pontuação:{} ---- Pontuação máxima:{}'.format(pontos,
                                                                pontuacao_maxima), align='center', font=('Courier', 20, 'normal'))

    for index in range(len(segmento)-1, 0, -1):
        x = segmento[index-1].xcor()
        y = segmento[index-1].ycor()
        segmento[index].goto(x, y)

    # Move o segmento 0 pra onde a cabeça esta
    if len(segmento) > 0:
        x = head.xcor()
        y = head.ycor()
        segmento[0].goto(x, y)

    movimento()

    # Checa a colisão entre a cabeça da cobra e o corpo
    for partes in segmento:
        if partes.distance(head) < 20:
            time.sleep(0.5)
            head.goto(0, 0)
            head.direction = 'stop'

            for parte in segmento:
                parte.goto(1000, 1000)

            segmento.clear()

            # Reseta a velocidade
            delay = 0.1

            # Reseta a pontuação
            pontos = 0

            caneta.clear()
            caneta.write('Pontuação:{} ---- Pontuação máxima:{}'.format(pontos,
                                                                        pontuacao_maxima), align='center', font=('Courier', 20, 'normal'))

    time.sleep(delay)


window.mainloop()
