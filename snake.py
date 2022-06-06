import random
import pygame
from pygame.locals import *

def posicao_aleatoria():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return(x//10 * 10, y//10 * 10) # 270, num inteiro

def colisao(c1,  c2):
    return (c1[0] == c2[0] and (c1[1] == c2[1]))


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# tela
pygame.init()
tela = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')

img = pygame.image.load('cobraa.png')
pygame.display.set_icon(img)

snake_cobra = [(200,200), (210,200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,105,180)) # cor da cobra

fruit_pos = posicao_aleatoria() # posição
fruit = pygame.Surface((10,10))
fruit.fill((0,255,0)) # cor da fruta

direction = LEFT

# limitar fps da snake/cobra
fps = pygame.time.Clock()

while True:
    fps.tick(10)
    for event in pygame.event.get():
        # clicar no quit, fechar jogo.
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                direction = UP

        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                direction = DOWN

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                direction = LEFT

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                direction = RIGHT

    if colisao(snake_cobra[0], fruit_pos):
        fruit_pos = posicao_aleatoria()
        snake_cobra.append((0,0))

    for i in range(len(snake_cobra) - 1, 0, -1):
        snake_cobra[i] = (snake_cobra[i-1][0], snake_cobra[i-1][1])

    # cima / y diminui
    if direction == UP:
        snake_cobra[0] = (snake_cobra[0][0], snake_cobra[0][1] - 10)

    # baixo
    if direction == DOWN:
        snake_cobra[0] = (snake_cobra[0][0], snake_cobra[0][1] + 10)

    # direita
    if direction == RIGHT:
        snake_cobra[0] = (snake_cobra[0][0] + 10, snake_cobra[0][1])

    # esquerda
    if direction == LEFT:
        snake_cobra[0] = (snake_cobra[0][0] - 10, snake_cobra[0][1])

    tela.fill((0, 0, 0))
    tela.blit(fruit, fruit_pos)
    for pos in snake_cobra:
        tela.blit(snake_skin, pos)

    pygame.display.update()