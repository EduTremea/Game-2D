from this import d
from tkinter import LEFT, RIGHT
import pygame, random
from pygame.locals import*

#definição para a maça sempre ficar alinhada nos pixels
def alinhado():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 * 10, y//10 * 10)

def colisao(c1,c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()

display = pygame.display.set_mode((800,600))
pygame.display.set_caption("Cobrinha")

#tamanho e cor da cobra
snake = [(200,200), (210,200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255))

#tamanho e cor da maça
apple_posicao = alinhado()
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

#ela sempre vai nascer se movimentando para a direita
direcao = RIGHT

clock = pygame.time.Clock() #taxa de fps

while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                direcao = UP
            if event.key == K_DOWN:
                direcao = DOWN
            if event.key == K_LEFT:
                direcao = LEFT
            if event.key == K_RIGHT:
                direcao = RIGHT
    if colisao(snake[0],apple_posicao):
        apple_posicao = alinhado()
        snake.append((0,0))

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if direcao == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if direcao == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if direcao == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if direcao == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])


    display.fill((0,0,0))
    display.blit(apple,apple_posicao)
    for pos in snake:
        display.blit(snake_skin,pos)
    
    pygame.display.update()