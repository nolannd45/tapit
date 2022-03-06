import pygame
import os
import sys
from random import randint
import time
import Fonction



pygame.init()
pygame.display.set_caption("Don't tap it !") # nom de la fenetre

couleur_fenetre = (255,255,255) # code de la couleur
screen = pygame.display.set_mode((700,700)) #taille fenetre
screen.fill(couleur_fenetre) #remplir la fenetre avec une couleur

#images :

# sons :



couleur_point = (127,127,127)

pygame.display.flip() #mettre a jour l'affichage pour la couleur

#code pour garder la fenetre ouverte

board = [[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]

def creer_quadrillage():
    u=175
    for y in range(1,5):
        pygame.draw.line(screen, (169,169,169), [0,u*y], [700,u*y])
    for x in range(1,5):
        pygame.draw.line(screen, (169,169,169), [u*x,0], [u*x,700])

def find_on_board(lists):
    res = 0
    for l in lists:
        res += l.count(1)
    return res
                

def delete_square():
    pos = pygame.mouse.get_pos()
    black_squares = get_square_board()
    for index in black_squares:
        if pos[0] > index[1]*175 and pos[0] <= (index[1]+1)*175:
            if pos[1] > index[0]*175 and pos[1] <= (index[0]+1)*175:
                pygame.draw.rect(screen, (255,255,255), pygame.Rect(index[1]*175 ,index[0]*175, 175, 175))
                board[index[0]][index[1]] = 0
                var_memoire = (index[0], index[1])
                return var_memoire 

def put_random_square(var_memoire):
    # à opti fdp : https://stackoverflow.com/questions/29804599/python-random-number-excluding-one-variables
    y = randint(0,3)
    x = randint(0,3)
    while board[y][x] == 1 or var_memoire == (y,x):
        y = randint(0,3)
        x = randint(0,3)
    pygame.draw.rect(screen , (0,0,0), pygame.Rect(x*175,y*175,175,175))
    board[y][x] = 1

def get_square_board():
    res = []
    for y in range(4):
        for x in range(4):
            if board[y][x] == 1:
               res.append([y,x])
    return res


def fade_out(largeur, longueur):
    fade = pygame.Surface((largeur, longueur))
    fade.fill((0, 0, 0))
    for alpha in range(0, 30):
        fade.set_alpha(alpha)
        screen.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.wait(5)

def game_lost():
    ...

        


launched = True
a = (0,0)
creer_quadrillage()
game = "True"
score = 0
while launched:
    if game == "True":
        while find_on_board(board) < 3:
            put_random_square(a)
            creer_quadrillage()
            pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                launched = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if screen.get_at(pygame.mouse.get_pos()) == (255,255,255):   
                    
                    fade_out(700, 700)
                    game = "inter"
                else :
                    score = score + 1
                    print(score)
                    a = delete_square()
                    creer_quadrillage()
    if game == "inter":
        game = "False"
    if game == "False":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                launched = False
                
          
    pygame.display.flip()



pygame.display.flip()


