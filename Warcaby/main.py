import pygame, sys, random, copy
from pygame.locals import *
from random import randint

pygame.init()

SZARY = (200,200,200)
BIALY = (255,255,255)
CSZARY = (100,100,100)
CZARNY = (0,0,0)
CBRAZ = (145, 78, 0)
BRAZ = (191, 108, 11)
ZOLYT = (255, 238, 0)

wielkosc = 90

okienko = pygame.display.set_mode((wielkosc * 8, wielkosc * 8))

plansza = [
    [0,2,0,2,0,2,0,2],
    [2,0,2,0,2,0,2,0],
    [0,2,0,2,0,2,0,2],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [1,0,1,0,1,0,1,0],
    [0,1,0,1,0,1,0,1],
    [1,0,1,0,1,0,1,0]
]

aktpos = [0,0]
bicie = False

def show_pionek(x,y,c):
    if c > 2:
        pygame.draw.rect(okienko,ZOLYT,(x*wielkosc,y*wielkosc,wielkosc,wielkosc))
    if c%2 == 1:
        color = BIALY
    elif c%2 == 0:
        color = CSZARY
    if c<5:
        pygame.draw.circle(okienko,CZARNY,(x*wielkosc + int(wielkosc/2),y*wielkosc + int(wielkosc/2)), int(wielkosc/2 - 5))
        pygame.draw.circle(okienko,color,(x*wielkosc + int(wielkosc/2),y*wielkosc + int(wielkosc/2)), int(wielkosc/2 - 10))

def show_pole(x,y):
    if(x%2 == 1 and y%2 == 1) or (x%2 == 0 and y%2 == 0):
        color = CBRAZ
    else:
        color = BRAZ
    pygame.draw.rect(okienko,color,(x*wielkosc,y*wielkosc,wielkosc,wielkosc))
    if plansza[y][x] == 5:
        pygame.draw.rect(okienko,ZOLYT,(x*wielkosc,y*wielkosc,wielkosc,wielkosc))
    if plansza[y][x] > 0:
        show_pionek(x,y,plansza[y][x])

def check_move(x,y):
    if 0<=x<=8 and 0<=y<=8:
        if plansza[y][x]%2 == 1:
            if 0<=x-1<8 and 0<=y-1<8:
                if plansza[y-1][x-1] == 0:
                    if not bicie:
                        plansza[y-1][x-1] = 5
                elif 0<=x-2<8 and 0<=y-2<8 and 5>plansza[y-1][x-1] > 0 and plansza[y-1][x-1] != plansza[y][x] - 2:
                    if plansza[y-2][x-2] == 0:
                        plansza[y-2][x-2] = 5
            if 0<=x+1<8 and 0<=y-1<8:
                if plansza[y-1][x+1] == 0:
                    if not bicie:
                        plansza[y-1][x+1] = 5
                elif 0<=x+2<8 and 0<=y-2<8 and 5>plansza[y-1][x+1] > 0 and plansza[y-1][x+1] != plansza[y][x] - 2:
                    if plansza[y-2][x+2] == 0:
                        plansza[y-2][x+2] = 5
            if 0<=x+1<8 and 0<=y+1<8:
                if 0<=x+2<8 and 0<=y+2<8 and 5>plansza[y+1][x+1] > 0 and plansza[y+1][x+1] != plansza[y][x] - 2:
                    if plansza[y+2][x+2] == 0:
                        plansza[y+2][x+2] = 5
            if 0<=x-1<8 and 0<=y+1<8:
                if 0<=x-2<8 and 0<=y+2<8 and 5>plansza[y+1][x-1] > 0 and plansza[y+1][x-1] != plansza[y][x] - 2:
                    if plansza[y+2][x-2] == 0:
                        plansza[y+2][x-2] = 5
        if plansza[y][x]%2 == 0:
            if 0<=x-1<8 and 0<=y+1<8:
                if plansza[y+1][x-1] == 0:
                    if not bicie:
                        plansza[y+1][x-1] = 5
                elif 0<=x-2<8 and 0<=y+2<8 and 5>plansza[y+1][x-1] > 0 and plansza[y+1][x-1] != plansza[y][x] - 2:
                    if plansza[y+2][x-2] == 0:
                        plansza[y+2][x-2] = 5
            if 0<=x+1<8 and 0<=y+1<8:
                if plansza[y+1][x+1] == 0:
                    if not bicie:
                        plansza[y+1][x+1] = 5
                elif 0<=x+2<8 and 0<=y+2<8 and 5>plansza[y+1][x+1] > 0 and plansza[y+1][x+1] != plansza[y][x] - 2:
                    if plansza[y+2][x+2] == 0:
                        plansza[y+2][x+2] = 5
            if 0<=x-1<8 and 0<=y-1<8:
                if 0<=x-2<8 and 0<=y-2<8 and 5>plansza[y-1][x-1] > 0 and plansza[y-1][x-1] != plansza[y][x] - 2:
                    if plansza[y-2][x-2] == 0:
                        plansza[y-2][x-2] = 5
            if 0<=x+1<8 and 0<=y-1<8:
                if 0<=x+2<8 and 0<=y-2<8 and 5>plansza[y-1][x+1] > 0 and plansza[y-1][x+1] != plansza[y][x] - 2:
                    if plansza[y-2][x+2] == 0:
                        plansza[y-2][x+2] = 5

def czysc():
    for i in range(8):
        for j in range(8):
            if plansza[i][j] == 5:
                plansza[i][j] = 0

def koniec_bicia():
    w = 0
    for row in plansza:
        for pole in row:
            if 2<pole<6:
                w = w + 1
    if w == 1:
        return True
    return False

m1 = False
zazn = False
kolej = 1

while 1:

    okienko.fill(SZARY)
    pos = list(pygame.mouse.get_pos())
    mouse = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_p:
            print(plansza)

    for i in range(8):
        for j in range(8):
            show_pole(i,j)

    if mouse[0]:
        if not m1:
            if not zazn:
                aktpos = [int(pos[1]/wielkosc),int(pos[0]/wielkosc)]
            if 3>plansza[aktpos[0]][aktpos[1]]>0 and not zazn and plansza[aktpos[0]][aktpos[1]] == kolej:
                plansza[aktpos[0]][aktpos[1]] = plansza[aktpos[0]][aktpos[1]] + 2
                zazn = True
            elif 2<plansza[aktpos[0]][aktpos[1]]<5 and zazn:
                plansza[aktpos[0]][aktpos[1]] = plansza[aktpos[0]][aktpos[1]] - 2
                if plansza[int(pos[1]/wielkosc)][int(pos[0]/wielkosc)] == 5:
                    plansza[int(pos[1]/wielkosc)][int(pos[0]/wielkosc)] = plansza[aktpos[0]][aktpos[1]]
                    plansza[aktpos[0]][aktpos[1]] = 0
                    if abs(int(pos[1]/wielkosc) - aktpos[0]) == 2:
                        plansza[int((aktpos[0] + pos[1]/wielkosc)/2)][int((aktpos[1] + pos[0]/wielkosc)/2)] = 0
                        bicie = True
                        if kolej == 1:
                            kolej = 2
                        else:
                            kolej = 1
                        aktpos = [int(pos[1]/wielkosc),int(pos[0]/wielkosc)]
                        plansza[aktpos[0]][aktpos[1]] = plansza[aktpos[0]][aktpos[1]] + 2
                    if kolej == 1:
                        kolej = 2
                    else:
                        kolej = 1
                if not bicie:
                    zazn = False
                czysc()
            m1 = True
    else:
        m1 = False

    if zazn:
        check_move(aktpos[1],aktpos[0])

    if koniec_bicia():
        bicie = False
        if kolej == 1:
            kolej = 2
        else:
            kolej = 1
        plansza[aktpos[0]][aktpos[1]] = plansza[aktpos[0]][aktpos[1]] - 2
        zazn = False

    pygame.display.update()