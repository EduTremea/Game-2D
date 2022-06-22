from this import d
from tkinter import LEFT, RIGHT
import pygame
import random
from pygame.locals import*

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
WINDOW_SIZE = (800, 600)
PIXEL_SIZE = 10

#definição para a maça sempre ficar alinhada nos pixels
def alinhado():
    x = random.randint(0, 580)
    y = random.randint(0, 580)
    return (x//10 * 10, y//10 * 10)


def colisao(c1, c2):
    pixelsX = list(range(c2[0], c2[0]+60))
    pixelsY = list(range(c2[1], c2[1]+60))
    
    if c1[0] in pixelsX:
        if c1[1] in pixelsY:
            return True


def limites_tela(pos):
    if 0 <= pos[0] < WINDOW_SIZE[0] and 0 <= pos[1] < WINDOW_SIZE[1]:
        return False
    else:
        return True



pygame.init()
pygame.font.init()

branco = (255, 255, 255)
font = pygame.font.SysFont('Comic Sans MS', 30)

game_icon = pygame.image.load("assets/icon.ico")
pygame.display.set_icon(game_icon)

trilha = pygame.mixer.music.load("assets/sound track.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)


screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Cobrinha Devoradora de Galáxias")

bg = pygame.image.load("assets/fundo.jpg")
screen.blit(bg, (0, 0))
pygame.transform.scale(bg, (0, 0))


# tamanho e cor da cobra
snake_pos = [(250, 50), (260, 50), (270, 50)]
snake_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
snake_surface.fill((204, 0, 204))  # cor

# ela sempre vai nascer se movimentando para a direita
direcao = RIGHT

# tamanho e cor da maça
apple_posicao = alinhado()
maca = pygame.image.load("assets/maca 60.png")
maca_surface = pygame.Surface((60, 60))


clock = pygame.time.Clock()  # taxa de fps


def restart_game():
    global snake_pos
    global apple_pos
    global snake_direction
    snake_pos = [(250, 50), (260, 50), (270, 50)]
    direcao = RIGHT
    apple_posicao = alinhado()


while True:   
    clock.tick(18)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()

        if event.type == KEYDOWN:
            if event.key == K_UP and direcao != DOWN:
                direcao = UP
            if event.key == K_DOWN and direcao != UP:
                direcao = DOWN
            if event.key == K_LEFT and direcao != RIGHT:
                direcao = LEFT
            if event.key == K_RIGHT and direcao != LEFT:
                direcao = RIGHT    

    if colisao(snake_pos[0], apple_posicao):
        apple_posicao = alinhado()
        snake_pos.append((0, 0))   

    for i in range(1,len(snake_pos)):
        if snake_pos[0] == snake_pos[i]:
            restart_game()             

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

    screen.blit(bg, (0, 0))
    pontos = font.render(f'Pontos:{len(snake_pos)-3}', False, branco)
    screen.blit(pontos,(0,-10))

    screen.blit(maca, apple_posicao)
    for pos in snake_pos:
        screen.blit(snake_surface, pos)



    pygame.display.update()
