import pygame, sys, random
from pygame.locals import *
from random import randint

pygame.init()

difficulty = 2
size = 25
boxsize = 40
nbombs = size * difficulty

jszary = (200,200,200)
szary = (127,127,127)
bialy = (255,255,255)
czarny = (0,0,0)
czerwony = (200,0,0)
niebieski = (0,0,200)
zielony = (0,200,0)
cniebieski = (0,0,100)
cczerwony = (100,0,0)
turkusowy = (64,224,208)

kolory = [niebieski, zielony, czerwony, cniebieski, cczerwony, turkusowy, czarny, jszary]

czcionka = pygame.font.SysFont("Comic Sans MS", 30)
congratulations = czcionka.render("Congratulations",True,zielony)
r2restart = czcionka.render("R - restart", True, niebieski)

class pole:
    def __init__(self):
        self.bomb = False
        self.adjBombs = 0
        self.revealed = False
        self.flagged = False

plansza = [[pole() for n in range(size)] for n in range (size)]

okienko = pygame.display.set_mode((size*boxsize, size*boxsize))
pygame.display.set_caption('Saper')

licznikFlag = 0

def inbounds(y,x):
    if x > -1 and x < size and y > -1 and y < size:
        return True
    return False

def adjBombsCounter(y,x):
    ite = [-1,0,1]
    w = 0
    for dy in ite:
        for dx in ite:
            if (dy or dx) and inbounds(y+dy,x+dx) and plansza[y+dy][x+dx].bomb:
                w += 1
    return w

def setup():
    global licznikFlag
    global loop
    licznikFlag = 0
    loop = True

    for n in range(nbombs):
        while 1:
            x = randint(0,size-1)
            y = randint(0,size-1)
            if not plansza[y][x].bomb:
                plansza[y][x].bomb = True
                break

    for y in range(size):
        for x in range(size):
            plansza[y][x].adjBombs = adjBombsCounter(y,x)

def reveal(pos):
    x = int(pos[0])
    y = int(pos[1])
    p = plansza[y][x]
    if not p.flagged:
        p.revealed = True

    if not p.bomb and not p.adjBombs:
        ite = [-1,0,1]
        for dy in ite:
            for dx in ite:
                if inbounds(y+dy,x+dx) and not plansza[y+dy][x+dx].revealed and not plansza[y+dy][x+dx].flagged:
                    reveal([x+dx,y+dy])
    
    if p.bomb:
        for row in plansza:
            for tile in row:
                tile.revealed = True

def flag(pos):
    global licznikFlag
    x = int(pos[0])
    y = int(pos[1])
    p = plansza[y][x]
    v = p.flagged
    if v:
        p.flagged = False
        licznikFlag -= 1
    if not p.revealed and not v:
        p.flagged = True
        licznikFlag +=1

def middle(pos):
    x = int(pos[0])
    y = int(pos[1])
    p = plansza[y][x]
    noFlags = 0
    ite = [-1,0,1]
    for dy in ite:
        for dx in ite:
            if inbounds(y+dy,x+dx) and (dy or dx) and plansza[y+dy][x+dx].flagged:
                noFlags += 1
    
    if noFlags == p.adjBombs:
        for dy in ite:
            for dx in ite:
                if inbounds(y+dy,x+dx) and not plansza[y+dy][x+dx].revealed and not plansza[y+dy][x+dx].flagged:
                    reveal([x+dx,y+dy])

def sprawdzenie():
    for row in plansza:
        for tile in row:
            if not (tile.bomb and tile.flagged) and not (not tile.bomb and tile.revealed):
                return False
    
    return True

setup()

m1 = False
m2 = False
m3 = False

loop = True

while 1:
    okienko.fill(jszary)
    pos = list(pygame.mouse.get_pos())
    mouse = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_r:
            plansza = [[pole() for n in range(size)] for n in range (size)]
            setup()

    if loop:

        for y in range(size):
            for x in range(size):
                pygame.draw.rect(okienko,czarny,(x*boxsize, y*boxsize, boxsize, boxsize))
                pygame.draw.rect(okienko,jszary,(x*boxsize +1, y*boxsize +1, boxsize -2, boxsize -2))
                p = plansza[y][x]
                if p.flagged:
                    pygame.draw.polygon(okienko,czerwony,[(x*boxsize +4, y*boxsize + 2),(x*boxsize +4, y*boxsize + boxsize/2),((x+1)*boxsize -4, y*boxsize + boxsize/4)])
                    pygame.draw.line(okienko,czarny,(x*boxsize +4, y*boxsize + 2),(x*boxsize +4, (y+1)*boxsize - 4),2)
                if p.revealed:
                    pygame.draw.rect(okienko,szary,(x*boxsize + 2, y*boxsize + 2, boxsize - 4, boxsize - 4))
                    if p.bomb:
                        pygame.draw.circle(okienko,czarny,(x*boxsize + boxsize/2,y*boxsize + boxsize/2),(boxsize-10)/2)
                    elif p.adjBombs:
                        kolor = kolory[p.adjBombs -1]
                        napis = czcionka.render(str(p.adjBombs),True,kolor)
                        okienko.blit(napis,(x*boxsize + boxsize/4,y*boxsize))

        if mouse[0]:
            if not m1:

                reveal([pos[0] / boxsize, pos[1] / boxsize])
                m1 = True
        else:
            m1 = False
        
        if mouse[1]:
            if not m2:
                m2 = True
                middle([pos[0] / boxsize, pos[1] / boxsize])
        else:
            m2 = False

        if mouse[2]:
            if not m3:
                flag([pos[0] / boxsize, pos[1] / boxsize])
                m3 = True
        else:
            m3 = False

    else:
        okienko.blit(congratulations,(20,20))
        okienko.blit(r2restart,(40,60))

    if licznikFlag == nbombs:
        if sprawdzenie():
            loop = False


    pygame.display.update()