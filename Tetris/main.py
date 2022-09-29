import pygame, sys, random, copy
from pygame.locals import *
from random import randint

pygame.init()

wys = 25
szer = 10
plansza = [[0 for n in range(szer)] for n in range(wys)]

czcionka = pygame.font.SysFont("Comic Sans MS", 30)

niebieski = (0,255,255)
cniebieski = (0,0,150)
zolty = (255,255,0)
pomaranczowy = (255,140,0)
zielony = (0,255,0)
czerwony = (255,0,0)
fioletowy = (255,0,255)
cszary = (144,144,144)
szary = (200,200,200)
bcszary = (100,100,100)
czarny = (0,0,0)
bialy = (255,255,255)

Next = czcionka.render("Next:",True, czarny)
Holding = czcionka.render("Holding:",True,czarny)
YL = czcionka.render("You Loose",True,czerwony)
R = czcionka.render("R to restart",True,czerwony)
Score = czcionka.render("Score:",True,czarny)
Pauza = czcionka.render("Pause",True,czarny)
Lev = czcionka.render("Level:",True,czarny)

# plansza

poczatek = [180,130]
wielkosc = 30

# pola: 1 - I    2 - o   3 - L   4 - s   5 - 2   6 - T   7 - J

klocki = [
    [
        [0,1,0,0],
        [0,1,0,0],
        [0,1,0,0],
        [0,1,0,0]
    ],
    [
        [2,2],
        [2,2]
    ],
    [
        [0,3,0],
        [0,3,0],
        [0,3,3]
    ],
    [
        [0,4,0],
        [0,4,4],
        [0,0,4]
    ],
    [
        [0,0,5],
        [0,5,5],
        [0,5,0]
    ],
    [
        [0,0,0],
        [6,6,6],
        [0,6,0]
    ],
    [
        [0,7,0],
        [0,7,0],
        [7,7,0]
    ]
]

okienko = pygame.display.set_mode((30 * 22, 30 * 25 + 160))

#pygame.mixer.music.load('tertis.ogg')
#pygame.mixer.music.play(-1)

def inbound(x,y):
    if x < 0 or y < 0 or x > szer - 1 or y > wys - 1:
        return False
    return True

def show(pole, xy):
    x, y = xy
    if not inbound(x,y):
        return
    if pole == 1:
        color = niebieski
    elif pole == 2:
        color = zolty
    elif pole == 3:
        color = pomaranczowy
    elif pole == 4:
        color = zielony
    elif pole == 5:
        color = czerwony
    elif pole == 6:
        color = fioletowy
    elif pole == 7:
        color = cniebieski
    else:
        pass
    if pole > 0:
        pygame.draw.rect(okienko,bcszary,(poczatek[0] + x*wielkosc, poczatek[1] + y*wielkosc, wielkosc, wielkosc))
        pygame.draw.rect(okienko,color,(poczatek[0] + x*wielkosc + 1, poczatek[1] + y*wielkosc + 1, wielkosc-2, wielkosc-2))

def losuj_klocek():
    return randint(0,len(klocki)-1)

def check(klocek, x, y):
    for i in range(len(klocek)):
        for j in range(len(klocek)):
            if inbound(x+i,y+j) and plansza[y+j][x+i] > 0 and klocek[j][i] > 0:
                return False
            if klocek[j][i] > 0 and y+j > wys-1:
                return False
            if klocek[j][i] > 0 and (x+i < 0 or x+i >= szer):
                return False
    return True

nextk = copy.deepcopy(klocki[losuj_klocek()])
holding = copy.deepcopy(klocki[losuj_klocek()])
ok = copy.deepcopy(nextk)
nextk = copy.deepcopy(klocki[losuj_klocek()])
pomok = copy.deepcopy(ok)
xok = 3
yok = -3

def obrot():
    global ok
    global pomok
    for i in range(len(ok)):
        for j in range(len(ok)):
            ok[i][j] = pomok[len(ok)-1-j][i]
    pomok = copy.deepcopy(ok)

def check_obrot(klocek,x,y):
    pom = [[0 for n in range(len(klocek))] for n in range(len(klocek))]
    for i in range(len(klocek)):
        for j in range(len(klocek)):
            pom[i][j] = klocek[len(klocek)-1-j][i]
    return check(pom,x,y)

def show_next(nextk):
    okienko.blit(Next,(180+22*15+10,20))
    nextk_poczatek = [180+22*15,70]
    for i in range(len(nextk)):
        for j in range(len(nextk)):
            if nextk[j][i] == 1:
                color = niebieski
            elif nextk[j][i] == 2:
                color = zolty
                nextk_poczatek = [180+24*15,100]
            elif nextk[j][i] == 3:
                color = pomaranczowy
            elif nextk[j][i] == 4:
                color = zielony
            elif nextk[j][i] == 5:
                color = czerwony
            elif nextk[j][i] == 6:
                color = fioletowy
            elif nextk[j][i] == 7:
                color = cniebieski
            else:
                pass
            if nextk[j][i] > 0:
                pygame.draw.rect(okienko,bcszary,(nextk_poczatek[0] + i*wielkosc, nextk_poczatek[1] + j*wielkosc, wielkosc, wielkosc))
                pygame.draw.rect(okienko,color,(nextk_poczatek[0] + i*wielkosc + 1, nextk_poczatek[1] + j*wielkosc + 1, wielkosc-2, wielkosc-2))

def show_holding(holding):
    okienko.blit(Holding,(30+10,20))
    holding_poczatek = [30,70]
    for i in range(len(holding)):
        for j in range(len(holding)):
            if holding[j][i] == 1:
                color = niebieski
            elif holding[j][i] == 2:
                color = zolty
                holding_poczatek = [60,100]
            elif holding[j][i] == 3:
                color = pomaranczowy
            elif holding[j][i] == 4:
                color = zielony
            elif holding[j][i] == 5:
                color = czerwony
            elif holding[j][i] == 6:
                color = fioletowy
            elif holding[j][i] == 7:
                color = cniebieski
            else:
                pass
            if holding[j][i] > 0:
                pygame.draw.rect(okienko,bcszary,(holding_poczatek[0] + i*wielkosc, holding_poczatek[1] + j*wielkosc, wielkosc, wielkosc))
                pygame.draw.rect(okienko,color,(holding_poczatek[0] + i*wielkosc + 1, holding_poczatek[1] + j*wielkosc + 1, wielkosc-2, wielkosc-2))

def check_tetris(rzad):
    wynik = 0
    for pole in rzad:
        if pole > 0:
            wynik += 1
    if wynik == szer:
        return True
    return False

def show_wynik(wynik,level):
    w = czcionka.render(str(wynik),True,czerwony)
    okienko.blit(Score,(35,300))
    okienko.blit(w,(35,340))
    okienko.blit(Lev,(35,380))
    l = czcionka.render(str(level),True,czerwony)
    okienko.blit(l,(35,420))

ile_tetris = 0

przegrana = False
pprzegrana = False

licznik = 0

szybkosc_spadania = 70
tmp_ss = szybkosc_spadania

wynik = 0

level = 0

licznik_lin = 0

def restart():
    global plansza
    global nextk
    global holding
    global ok
    global pomok
    global xok
    global yok
    global przegrana
    global licznik
    global szybkosc_spadania
    global tmp_ss
    global wynik
    global level
    global pprzegrana
    global licznik_lin

    plansza = [[0 for n in range(szer)] for n in range(wys)]
    nextk = copy.deepcopy(klocki[losuj_klocek()])
    holding = copy.deepcopy(klocki[losuj_klocek()])

    ok = copy.deepcopy(nextk)
    nextk = copy.deepcopy(klocki[losuj_klocek()])
    pomok = copy.deepcopy(ok)
    xok = 3
    yok = -3

    przegrana = False
    pprzegrana = False
    
    licznik = 0

    szybkosc_spadania = 70
    tmp_ss = szybkosc_spadania

    wynik = 0

    level = 0

    licznik_lin = 0

while 1:
    okienko.fill(bialy)
    pygame.draw.rect(okienko,czarny,(poczatek[0] - 2, poczatek[1] - 2, szer * wielkosc + 4, wys * wielkosc + 4))

    if pprzegrana:
        okienko.blit(YL,(500,300))
        okienko.blit(R,(485,340))

    if przegrana:
        okienko.blit(Pauza,(500,400))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_LEFT:
            if check(ok,xok-1,yok) and not przegrana:
                xok -= 1
        if event.type == KEYDOWN and event.key == K_RIGHT:
            if check(ok,xok+1,yok) and not przegrana:
                xok += 1
        if event.type == KEYDOWN and event.key == K_DOWN:
            tmp_ss = szybkosc_spadania
            szybkosc_spadania = 10
            licznik = 0
        if event.type == KEYUP and event.key == K_DOWN:
            szybkosc_spadania = tmp_ss
        if event.type == KEYDOWN and event.key == K_UP:
            if check_obrot(ok,xok,yok) and not przegrana:
                obrot()
        if event.type == KEYDOWN and event.key == K_SPACE:
            if check(holding,xok,yok) and not przegrana:
                ok, holding = holding, ok
                pomok = copy.deepcopy(ok)
        if event.type == KEYDOWN and event.key == K_r and pprzegrana:
            restart()
        if event.type == KEYDOWN and event.key == K_p:
            if przegrana:
                przegrana = False
            else:
                przegrana = True

    for i in range(wys):
        for j in range(szer):
            pygame.draw.rect(okienko,cszary,(poczatek[0] + j*wielkosc, poczatek[1] + i*wielkosc, wielkosc, wielkosc))
            pygame.draw.rect(okienko,szary,(poczatek[0] + j*wielkosc + 1, poczatek[1] + i*wielkosc + 1, wielkosc-2, wielkosc-2))
            show(plansza[i][j],(j,i))
    
    for i in range(len(ok)):
        for j in range(len(ok)):
            show(ok[i][j],(xok + j,yok + i))
    
    show_next(nextk)
    show_holding(holding)
    show_wynik(wynik,level)

    if licznik == szybkosc_spadania and not przegrana:
        if check(ok,xok,yok+1):
            yok += 1
        else:
            for i in range(len(ok)):
                for j in range(len(ok)):
                    if inbound(xok+i,yok+j) and ok[j][i] > 0:
                        plansza[yok + j][xok + i] = ok[j][i]
                    elif ok[j][i] > 0:
                        przegrana = True
                        pprzegrana = True
            ok = copy.deepcopy(nextk)
            nextk = copy.deepcopy(klocki[losuj_klocek()])
            pomok = copy.deepcopy(ok)
            xok = 3
            yok = -3
        licznik = 0
    
    for i in range(len(plansza)):
        if check_tetris(plansza[i]):
            plansza.pop(i)
            plansza.insert(0,[0 for n in range(szer)])
            ile_tetris += 1
    
    if ile_tetris == 1:
        wynik += 40*(level+1)
    if ile_tetris == 2:
        wynik += 100*(level+1)
    if ile_tetris == 3:
        wynik += 300*(level+1)
    if ile_tetris == 4:
        wynik += 1200*(level+1)
    
    licznik_lin += ile_tetris
    ile_tetris = 0

    if licznik_lin >= 10:
        level += 1
        szybkosc_spadania -= 5
        licznik_lin -= 10

    pygame.display.update()
    if not przegrana:
        licznik += 1