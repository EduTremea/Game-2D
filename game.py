from this import d
from tkinter import LEFT, RIGHT
import pygame, random
from pygame.locals import*

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()

display = pygame.display.set_mode((800,600))
pygame.display.set_caption("Cobrinha")

snake = [(200,200), (210,200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255))

apple_posicao = (random.randint(0,590), random.randint(0,590))
apple = pygame.Surface((10,10))
apple.fill((255,0,0))


direcao = LEFT

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    display.fill((0,0,0))
    display.blit(apple,apple_posicao)
    for pos in snake:
        display.blit(snake_skin,pos)
    
    pygame.display.update()