from this import d
from tkinter import LEFT, RIGHT
import pygame, random
from pygame.locals import*

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
WINDOW_SIZE = (800, 600)
PIXEL_SIZE = 10

#definição para a maça sempre ficar alinhada nos pixels
def alinhado():
    x = random.randint(0,580)
    y = random.randint(0,580)
    return (x//10 * 10, y//10 * 10)

def colisao(c1,c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

def limites_tela(pos):
    if 0 <= pos[0] < WINDOW_SIZE[0] and 0 <= pos[1] < WINDOW_SIZE[1]:
        return False
    else:
        return True


pygame.init()

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Cobrinha")

#tamanho e cor da cobra
snake_pos = [(250, 50), (260, 50), (270, 50)]
snake_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
snake_surface.fill((255, 255, 255))

#ela sempre vai nascer se movimentando para a direita
direcao = RIGHT

#tamanho e cor da maça
apple_posicao = alinhado()
apple = pygame.Surface((10,10))
apple.fill((255,0,0))


clock = pygame.time.Clock() #taxa de fps

def restart_game():
    global snake_pos
    global apple_pos
    global snake_direction
    snake_pos = [(250, 50), (260, 50), (270, 50)]
    direcao = RIGHT
    apple_posicao = alinhado()

while True:
    clock.tick(20)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                direcao = UP
            if event.key == K_DOWN:
                direcao = DOWN
            if event.key == K_LEFT:
                direcao = LEFT
            if event.key == K_RIGHT:
                direcao = RIGHT

    if colisao(snake_pos[0],apple_posicao):
        apple_posicao = alinhado()
        snake_pos.append((0,0))


    for i in range(len(snake_pos) - 1, 0, -1):
        snake_pos[i] = (snake_pos[i-1][0], snake_pos[i-1][1])

    if limites_tela(snake_pos[0]):
        restart_game()

    if direcao == UP:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] - 10)
    if direcao == DOWN:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] + 10)
    if direcao == RIGHT:
        snake_pos[0] = (snake_pos[0][0] + 10, snake_pos[0][1])
    if direcao == LEFT:
        snake_pos[0] = (snake_pos[0][0] - 10, snake_pos[0][1])


    screen.fill((0,0,0))
    screen.blit(apple,apple_posicao)
    for pos in snake_pos:
        screen.blit(snake_surface,pos)
    
    pygame.display.update()