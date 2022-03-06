import pygame
import os
import sys
from random import randint
import time
import Fonction



pygame.init()
pygame.display.set_caption("Don't tap it !") # nom de la fenetre

couleur_fenetre = (255,255,255) # code de la couleur
screen = pygame.display.set_mode((700,800)) #taille fenetre
screen.fill(couleur_fenetre) #remplir la fenetre avec une couleur

#images :

red = (213, 50, 80)

# sons :



couleur_point = (127,127,127)

pygame.display.flip() #mettre a jour l'affichage pour la couleur



def resetB(board):
    board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

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
                

def delete_square(board):
    pos = pygame.mouse.get_pos()
    black_squares = get_square_board(board)
    for index in black_squares:
        if pos[0] > index[1]*175 and pos[0] <= (index[1]+1)*175:
            if pos[1] > index[0]*175 and pos[1] <= (index[0]+1)*175:
                pygame.draw.rect(screen, (255,255,255), pygame.Rect(index[1]*175 ,index[0]*175, 175, 175))
                board[index[0]][index[1]] = 0
                var_memoire = (index[0], index[1])
                return var_memoire 

def put_random_square(var_memoire,board):
    y = randint(0,3)
    x = randint(0,3)
    while board[y][x] == 1 or var_memoire == (y,x):
        y = randint(0,3)
        x = randint(0,3)
    pygame.draw.rect(screen , (0,0,0), pygame.Rect(x*175,y*175,175,175))
    board[y][x] = 1

def get_square_board(board):
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

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def updateScore(score):
    sc = pygame.draw.rect(screen, couleur_fenetre, pygame.Rect(0, 750, 250, 50)) 
    pygame.display.flip()
    affScore = score_font.render("Your Score: " + str(score), True, red)
    screen.blit(affScore, [0, 750])

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, red)
    screen.blit(value, [0, 0])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [700 / 6, 700 / 3])

def classement():
    i=0
    classement = []
    fichier = open ("./classement.txt","r")
    for line in fichier:
        classement.append(int(line))
    fichier.close()
    return classement

def affichageClass(classement):
    i=0
    for line in classement:
        i=i+1
        value = score_font.render(str(i)+" - " + str(line), True, red)
        screen.blit(value, [300, 300+i*30])

        

def jeu():
    screen.fill(couleur_fenetre)
    board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    launched = True
    game_close = False
    a = (0,0)
    creer_quadrillage()
    score = 0
    while launched:

        while game_close == True:
            screen.fill(couleur_fenetre)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(score)
            affichageClass(classement())
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                    if event.key == pygame.K_c:
                        jeu()

        while find_on_board(board) < 3:
            put_random_square(a,board)
            creer_quadrillage()
            pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                launched = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if screen.get_at(pygame.mouse.get_pos()) == (255,255,255):  
                    fade_out(700,800)
                    resetB(board)
                    game_close = True
                else :
                    updateScore(score)
                    score = score + 1
                    print(score)
                    a = delete_square(board)
                    creer_quadrillage()
        pygame.display.update()

def button(screen, position, text):
    font = pygame.font.SysFont("Arial", 50)
    text_render = font.render(text, 1, (255, 0, 0))
    x, y, w , h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(screen, (100, 100, 100), (x, y, w , h))
    return screen.blit(text_render, (x, y))

def menu():
    """ This is the menu that waits you to click the s key to start """
    b1 = button(screen, (150, 400), "Quit")
    b2 = button(screen, (500, 400), "Start")
    message("Welcome to Don't tap it ! Press start to play ", red)
    menu = True
    while menu:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                key_to_start = event.key == pygame.K_s or event.key == pygame.K_RIGHT or event.key == pygame.K_UP
                if key_to_start:
                   jeu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b2.collidepoint(pygame.mouse.get_pos()):
                    jeu()
                elif b1.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                
                    
        pygame.display.update()
    pygame.quit()


menu()


