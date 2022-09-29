# -*- coding: utf-8 -*-
import pygame, sys, copy
from pygame.locals import *

pygame.init()

size = 50  #>=14
additional_space = 150
szybkosc = 50
sizerec = 20

xu = 30
yu = 50

bialy = (255,255,255)
szary = (211,211,211)
jszary = (128,128,128)
czarny = (0,0,0)
czerwony = (200,0,0)

okienko = pygame.display.set_mode((size*sizerec + additional_space,size*sizerec))
pygame.display.set_caption('Game of Life')

czcionka = pygame.font.SysFont("Comic Sans MS", 30)
czcionka2 = pygame.font.SysFont("Comic Sans MS", 20)
settings = czcionka.render("Settings",True,czarny)
A = czcionka.render("A",True,czarny)
B = czcionka.render("B",True,czarny)
stop = czcionka.render("Stopped",True,czerwony)
play = czcionka.render("Playing",True,czarny)

tab = [[-1]*size for x in range(size)]
ite = [-1,0,1]

a = [False,False,True,True,False,False,False,False,False]
b = [False,False,False,True,False,False,False,False,False]
mouseclick = False

pause = 1

licznik = 0


def check_box (y,x):
    count_alive = 0
    for dy in ite:
        for dx in ite:
                if tab[(dy+y)%size][(dx+x)%size] == 1:
                        count_alive += 1
    if tab[y][x] == 1:
        count_alive -= 1
    return count_alive

def draw():
    px = additional_space
    y = 0
    x = px
    for row in tab:
        for elem in row:
            if elem == 1:
                kolor = bialy
            else:
                kolor = jszary
            pygame.draw.rect(okienko,szary,(x,y,sizerec,sizerec))
            pygame.draw.rect(okienko,kolor,(x+1,y+1,sizerec-2,sizerec-2))
            x += sizerec
        y += sizerec
        x = px

def ustawienia():
    okienko.blit(settings,(0,0))
    x = xu
    y = yu
    i = 0
    for pom in a:
        if pom:
            kolor = bialy
        else:
            kolor = jszary
        pygame.draw.rect(okienko,szary,(x,y,sizerec,sizerec))
        pygame.draw.rect(okienko,kolor,(x+1,y+1,sizerec-2,sizerec-2))
        n = czcionka2.render(str(i),True,czarny)
        okienko.blit(n,(x+5,y-5))
        y += sizerec
        i += 1
    okienko.blit(A,(x,y))

    i = 0
    x += sizerec*2
    y = yu
    for pom in b:
        if pom:
            kolor = bialy
        else:
            kolor = jszary
        pygame.draw.rect(okienko,szary,(x,y,sizerec,sizerec))
        pygame.draw.rect(okienko,kolor,(x+1,y+1,sizerec-2,sizerec-2))
        n = czcionka2.render(str(i),True,czarny)
        okienko.blit(n,(x+5,y-5))
        y += sizerec
        i += 1
    okienko.blit(B,(x,y))

while(1):
    pos = list(pygame.mouse.get_pos())
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_SPACE:
            pause *= -1
        if event.type == KEYDOWN and event.key == K_c:
            tab = [[-1]*size for x in range(size)]

    if pygame.mouse.get_pressed()[0]:
        if pos[0] >= additional_space:
            if not mouseclick:
                tab[int(pos[1]/sizerec)][int((pos[0]-additional_space)/sizerec)] *= -1
                mouseclick = True
        if pos[0] >= xu and pos[0] <= xu+sizerec and pos[1] >= yu and pos[1] <= yu + 9*sizerec:
            if not mouseclick:
                if a[(pos[1]-yu)/sizerec]:
                    a[(pos[1]-yu)/sizerec] = False
                else:
                    a[(pos[1]-yu)/sizerec] = True
                mouseclick = True
        if pos[0] >= xu+2*sizerec and pos[0] <= xu+3*sizerec and pos[1] >= yu and pos[1] <= yu + 9*sizerec:
            if not mouseclick:
                if b[(pos[1]-yu)/sizerec]:
                    b[(pos[1]-yu)/sizerec] = False
                else:
                    b[(pos[1]-yu)/sizerec] = True
                mouseclick = True
    else:
        mouseclick = False

    if licznik > szybkosc and pause == -1:
        newtab = copy.deepcopy(tab)
        for y in range(size):
            for x in range(size):
                n = check_box(y,x)
                if tab[y][x] == 1:
                    if not a[n]:
                        newtab[y][x] *= -1
                else:
                    if b[n]:
                        newtab[y][x] *= -1
        tab = newtab
        licznik = 0


    okienko.fill(szary)
    draw()
    ustawienia()

    if pause == -1:
        okienko.blit(play,(5,size*sizerec-50))
        licznik += 1
    else:
        okienko.blit(stop,(0,size*sizerec-50))

    pygame.display.update()
