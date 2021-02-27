import pygame
from pygame.locals import *

W = (255, 255, 255)
R = (255, 0, 0)
G = (0, 255, 0)
B = (0, 0, 255)
J = (255, 255, 0)
C = (0, 255, 255)
M = (255, 0, 255)

key_dict = {K_r:R, K_g:G, K_b:B, K_j:J, K_c:C, K_m:M}

pygame.init()
screen = pygame.display.set_mode((700, 700))
background = W
screen.fill(background)
pygame.display.update()
color = (0, 0, 0)
drawing = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in key_dict:
                color = key_dict[event.key]
        if event.type == MOUSEBUTTONDOWN:
            drawing = True
        if event.type == MOUSEBUTTONUP:
            drawing = False
        if drawing == True:
            screen.set_at(event.pos, color)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                screen.fill(color)
            if event.key == pygame.K_e:
                screen.fill(W)
    
    pygame.display.update()

pygame.quit()
