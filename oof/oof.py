# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import random
from PIL import ImageFont
import sys

pygame.init()
pygame.mixer.init()

### KOLORY ###
sanes = (131, 236, 255)
biay = (255,255,255)
RED = (255,0,0)
czorny = (0,0,0)
szary = (127,127,127)
roz = (255, 71, 147)
zolty = (255,234,8)

### NAPISY ###
font = ImageFont.truetype("comic.ttf",30)
czcionka = pygame.font.SysFont("Comic Sans MS", 30)
rzycie = czcionka.render("Loif",True,biay)
napis = czcionka.render("Do u wanna hav a bad tom?", True,sanes)
gameover = czcionka.render("You dun goof! R to restart",True,biay)
hitormiss = czcionka.render("Hit or miss?",True,roz)
iguess = czcionka.render("I guess you always miss",True,roz)
huh = czcionka.render("HUH??",True,roz)

### OKNO ###
okienko = pygame.display.set_mode((800,800))
pygame.display.set_caption('sanes!!!')


### WCZYTYWANIE OBRAZKOW ###
tlo = pygame.image.load("res/tlo.png").convert_alpha()
sans1 = pygame.image.load("res/s1.png").convert_alpha()
sans2 = pygame.image.load("res/s2.png").convert_alpha()
sans3 = pygame.image.load("res/s3.png").convert_alpha()
serce = pygame.image.load("res/serce.png").convert_alpha()
kosc = pygame.image.load("res/kosc.png").convert_alpha()
atk1 = pygame.image.load("res/atk1.png").convert_alpha()
atk2 = pygame.image.load("res/atk2.png").convert_alpha()
item1 = pygame.image.load("res/item1.png").convert_alpha()
item2 = pygame.image.load("res/item2.png").convert_alpha()
tom = pygame.image.load("res/tom.png").convert_alpha()
a1 = pygame.image.load("res/a1.png").convert_alpha()
a2 = pygame.image.load("res/a2.png").convert_alpha()
a3 = pygame.image.load("res/a3.png").convert_alpha()
a4 = pygame.image.load("res/a4.png").convert_alpha()
a5 = pygame.image.load("res/a5.png").convert_alpha()
a6 = pygame.image.load("res/a6.png").convert_alpha()
a7 = pygame.image.load("res/a7.png").convert_alpha()
devil = pygame.image.load("res/devil.png").convert_alpha()
victory = pygame.image.load("res/victory.png").convert_alpha()
loose = pygame.image.load("res/loose.png").convert_alpha()
przed_5_fala = pygame.image.load("res/przed_piata_fala.png").convert_alpha()
przed_10_fala = pygame.image.load("res/mniej_niz_10.png").convert_alpha()
pozniej = pygame.image.load("res/mniej_niz_20.png").convert_alpha()
przed_30 = pygame.image.load("res/przed_35.png").convert_alpha()
OwO = pygame.image.load("res/OwO.png").convert_alpha()

kosc1 = pygame.transform.scale(kosc,(500,15))
kosc2 = pygame.transform.rotate(kosc,90)
kosc2 = pygame.transform.scale(kosc2,(100,500))
tom = pygame.transform.scale(tom,(393,337))
a1 = pygame.transform.scale(a1,(671,529))
a2 = pygame.transform.scale(a2,(671,529))
a3 = pygame.transform.scale(a3,(671,529))
a4 = pygame.transform.scale(a4,(671,529))
a5 = pygame.transform.scale(a5,(671,529))
a6 = pygame.transform.scale(a6,(671,529))
a7 = pygame.transform.scale(a7,(671,529))
devil = pygame.transform.scale(devil,(415,415))

### MUZYKA ###
pygame.mixer.music.load("res/muzyka.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.4)
OOF1 = pygame.mixer.Sound("res/oof.ogg")
OOF2 = pygame.mixer.Sound("res/oof2.ogg")
OOF2.set_volume(0.5)
hit = pygame.mixer.Sound("res/hitormiss.ogg")

zegar = pygame.time.Clock()

sans = sans1
a = a1

kier_x = 0.2
kier_y = 0.2
x = 200
y = 560
kier_k_x = 0.3
kier_k_y = 0.2
kier_s_x = 0
przys_s_x = 0.01
porusz_sans = 1
pos_nazw = [(130, 520),(130, 570),(430,520),(430,570)]
to_pop = False

kosci1 = []
kosci2 = []
kosci3 = []

lew = False
pra = False
gor = False
dol = False
cz2_a = False
using = False
use = False
mozna = False
dodane = False
zmniejszone = False
ply = False
endless = False
unlock_endless = False
develooper = False

i = 0
predkosc_sansa = 20
x_sans = 150
j = 0
pojawianie = 300
czas_rundy = 0
dlugosc_rundy = 9415
timer_endless = dlugosc_rundy/2
ilosc_rund = 5
licznik_rund = 0
atak = 0
itemek = 0
badtom = 0
licznik_tom = 0
x_tom = 224
y_tom = 50
licznik_ataku = 0
predkosc_ataku = 20
licznik_cz2_a = 0
oczekiwanie1 = 40
licznik_INT = 0
czas_INT = 750
ile_atk = 0

rzydzie = 10000
odejmowanie = 5

### EKWIPUNEK ###
eq = [[u"LÖÖPS",20, "HP"],[u"Ślimor",42069, "ATK"],["Bitch Lasagna",40, "HP"],["Bullet",1,"ATK"]]

### NAJLEPSZY WYNIK ###
fh = open("res/best_score.txt","a")
fh.close()
fh = open("res/best_score.txt","r")
cos = fh.read()
if cos == "":
    fh.close()
    fh = open("res/best_score.txt","w")
    tst = ["0\n","0"]
    fh.writelines(tst)
    fh.close()
fh = open("res/best_score.txt","r")
plik = fh.readlines()
najlepszy_wynik = int(plik[0])
if plik[1] == "0":
    unlock_endless = False
else:
    unlock_endless = True
fh.close()


def koniec():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                fh = open("res/best_score.txt","w")
                plikw = [str(najlepszy_wynik) + "\n",str(int(unlock_endless))]
                fh.writelines(plikw)
                fh.close()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_r:
                return

while True:

    czas_rundy += 1
    pos = pygame.mouse.get_pos()
    czas = zegar.tick()

    ### PRZEGRANA ###
    if rzydzie<50 and not endless:
        if licznik_rund == 4:
            okienko.blit(loose,(0,0))
        else:
            okienko.blit(przed_5_fala,(0,0))
        pygame.mixer.music.stop()
        pygame.mixer.music.load("res/hymn.mp3")
        pygame.mixer.music.play()
        pygame.display.update()
        lew = False
        pra = False
        gor = False
        dol = False
        koniec()
        pygame.mixer.music.stop()
        pygame.mixer.music.load("res/muzyka.mp3")
        pygame.mixer.music.play()
        rzydzie = 10000
        czas_rundy = 0
        licznik_rund = 0
        kier_x = 0.2
        kier_y = 0.2
        x = 200
        y = 560
        kier_k_x = 0.3
        kier_k_y = 0.2
        kosci1 = []
        kosci2 = []
        kosci3 = []
        eq = [[u"LÖÖPS",20, "HP"],[u"Ślimor",42069, "ATK"],["Bitch Lasagna",40, "HP"],["Bullet",1,"ATK"]]
        ile_atk = 0
        endless = False
    elif endless and rzydzie<50:
        if licznik_rund > najlepszy_wynik:
            najlepszy_wynik = licznik_rund
            nap = czcionka.render(str(licznik_rund) + "   NEW BEST!!!",True,biay)
        else:
            nap = czcionka.render(str(licznik_rund),True,biay)
        if licznik_rund<10:
            okienko.blit(przed_10_fala,(0,0))
            okienko.blit(nap,(380,470))
        elif licznik_rund<20:
            okienko.blit(pozniej,(0,0))
            okienko.blit(nap,(300,450))
        elif licznik_rund<30:
            okienko.blit(przed_30,(0,0))
            okienko.blit(nap,(340,595))
        else:
            okienko.blit(OwO,(0,0))
            okienko.blit(nap,(350,690))
        pygame.display.update()
        pygame.mixer.music.stop()
        pygame.mixer.music.load("res/hymn.mp3")
        pygame.mixer.music.play()
        lew = False
        pra = False
        gor = False
        dol = False
        koniec()
        pygame.mixer.music.stop()
        pygame.mixer.music.load("res/muzyka.mp3")
        pygame.mixer.music.play()
        rzydzie = 10000
        czas_rundy = 0
        licznik_rund = 0
        kier_x = 0.2
        kier_y = 0.2
        x = 200
        y = 560
        kier_k_x = 0.3
        kier_k_y = 0.2
        kosci1 = []
        kosci2 = []
        kosci3 = []
        eq = [[u"LÖÖPS",20, "HP"],[u"Ślimor",42069, "ATK"],["Bitch Lasagna",40, "HP"],["Bullet",1,"ATK"]]
        ile_atk = 0
        endless = False

    
    ### ZAP�TLENIE PIOSENKI ###
    if pygame.mixer.music.get_busy() == False:
        pygame.mixer.music.play()

    for event in pygame.event.get():
        if event.type == QUIT:
            fh = open("res/best_score.txt","w")
            plikw = [str(najlepszy_wynik) + "\n",str(int(unlock_endless))]
            fh.writelines(plikw)
            fh.close()
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            fh = open("res/best_score.txt","w")
            plikw = [str(najlepszy_wynik) + "\n",str(int(unlock_endless))]
            fh.writelines(plikw)
            fh.close()
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_LEFT and not itemek:
            lew = True
        if event.type == KEYDOWN and event.key == K_RIGHT and not itemek:
            pra = True
        if event.type == KEYDOWN and event.key == K_UP and not itemek:
            gor = True
        if event.type == KEYDOWN and event.key == K_DOWN and not itemek:
            dol = True
        if event.type == KEYUP and event.key == K_LEFT:
            lew = False
        if event.type == KEYUP and event.key == K_RIGHT:
            pra = False
        if event.type == KEYUP and event.key == K_UP:
            gor = False
        if event.type == KEYUP and event.key == K_DOWN:
            dol = False
        if event.type == KEYDOWN and event.key == K_p and develooper:
            print(pos)
            print((x,y))
            print(czas_rundy)
        if event.type == KEYDOWN and event.key == K_t and develooper:
            czas_rundy = dlugosc_rundy
        if event.type == KEYDOWN and event.key == K_y and develooper:
            licznik_rund += 1
            ile_atk += 1
        if event.type == KEYDOWN and event.key == K_o and develooper:
            rzydzie = 49
        if event.type == KEYDOWN and event.key == K_e and unlock_endless:
            endless = True
        if event.type == KEYDOWN and event.key == K_u and develooper:
            if unlock_endless:
                unlock_endless = False
            else:
                unlock_endless = True
        if event.type == KEYDOWN and event.key == K_m:
            if develooper:
                develooper = False
            else:
                develooper = True

    okienko.fill(biay)
    okienko.blit(tlo,(0,0))
    okienko.blit(napis, (150,450))

    ### ANIMACJA ###
    if sans == sans1 and i == predkosc_sansa:
        sans = sans2
        i = 0
    else:
        if sans == sans2 and i == predkosc_sansa:
            sans = sans3
            i = 0
        else:
            if sans == sans3 and i == predkosc_sansa:
                sans = sans1
                i = 0
    okienko.blit(sans, (x_sans,-25))

    ### PORUSZANIE ###
    if lew and x>=110:
        x -= kier_x * czas
    if pra and x<=665:
        x += kier_x * czas
    if gor and y>=525:
        y -= kier_y * czas
    if dol and y<=580:
        y += kier_y * czas
    okienko.blit(serce, (x,y))

    ### WALKA ###
    if czas_rundy <= dlugosc_rundy or endless:

        if czas_rundy == dlugosc_rundy and not endless:
            licznik_rund += 1
        if czas_rundy == timer_endless and endless:
            licznik_rund += 1
            czas_rundy = 0

        ### KOSCI ###
        losowa = random.randint(0,3)
        if j > pojawianie:
            if losowa == 1:
                kosci1.append(list((random.randint(110,520),750,True)))
                j = 0
            else:
                if losowa == 2:
                    kosci2.append(list((-380,random.randint(525,600),True)))
                    j = 0
                else:
                    if losowa == 3:
                        kosci1.append(list((random.randint(110,520),750,True)))
                        j = 0
                    else:
                        kosci3.append(list((750,random.randint(525,600),True)))
                        j = 0


        for kosca in kosci1:
            if kosca[1] > 525 and kosca[2]:
                kosca[1] -= kier_k_y * czas
            else:
                kosca[1] += kier_k_y * czas
                kosca[2] = False
            tmp = (kosca[0],kosca[1])
            okienko.blit(kosc2,tmp)
            if x>kosca[0]-40 and x<kosca[0]+100 and y>kosca[1]-40 and y<kosca[1]+500:
                rzydzie -= odejmowanie
                OOF2.play()

        for kosca in kosci2:
            if kosca[0] < -20 and kosca[2]:
                kosca[0] += kier_k_x * czas
            else:
                kosca[0] -= kier_k_x * czas
                kosca[2] = False
            tmp = (kosca[0],kosca[1])
            okienko.blit(kosc1,tmp)
            if x>kosca[0]-40 and x<kosca[0]+500 and y>kosca[1]-40 and y<kosca[1]+15:
                rzydzie -= odejmowanie
                OOF2.play()

        for kosca in kosci3:
            if kosca[0] > 320 and kosca[2]:
                kosca[0] -= kier_k_x * czas
            else:
                kosca[0] += kier_k_x * czas
                kosca[2] = False
            tmp = (kosca[0],kosca[1])
            okienko.blit(kosc1,tmp)
            if x>kosca[0]-40 and x<kosca[0]+500 and y>kosca[1]-40 and y<kosca[1]+15:
                rzydzie -= odejmowanie
                OOF2.play()

    
    ### ATAK I ITEMY ###
    else:
        if licznik_rund < ilosc_rund:
            kosci1 = []
            kosci2 = []
            kosci3 = []
            if list(pos)[0] > 100 and list(pos)[0] < 300 and list(pos)[1] > 670 and list(pos)[1] < 770:
                atk = atk2
                if pygame.mouse.get_pressed()[0] and itemek == 0:
                    atak = 1
            else:
                atk = atk1
            okienko.blit(atk,(100,670))

            if list(pos)[0] > 500 and list(pos)[0] < 700 and list(pos)[1] > 670 and list(pos)[1] < 770:
                item = item2
                if pygame.mouse.get_pressed()[0] and atak == 0:
                    itemek = 1
            else:
                item = item1
            okienko.blit(item,(500,670))

            ### ATAK ###
            if atak:
                if cz2_a == False:
                    licznik_ataku += 1
                    if a == a1 and licznik_ataku > predkosc_ataku:
                        a = a2
                        licznik_ataku = 0
                    else:
                        if a == a2 and licznik_ataku > predkosc_ataku:
                            a = a3
                            licznik_ataku = 0
                        else:
                            if a == a3 and licznik_ataku > predkosc_ataku:
                                a = a4
                                licznik_ataku = 0
                            else:
                                if a == a4 and licznik_ataku > predkosc_ataku:
                                    a = a5
                                    licznik_ataku = 0
                                else:
                                    if a == a5 and licznik_ataku > predkosc_ataku:
                                        a = a6
                                        licznik_ataku = 0
                                    else:
                                        if a == a6 and licznik_ataku > predkosc_ataku:
                                            a = a7
                                            licznik_ataku = 0
                                        else:
                                            if a == a7 and licznik_ataku > predkosc_ataku:
                                                a = False

                    if a:
                        okienko.blit(a,(100,25))

                    kier_s_x += przys_s_x
                    if x_sans > -70 and porusz_sans:
                        x_sans -= kier_s_x * czas
                    else:
                        if porusz_sans:
                            kier_s_x = 0
                        if x_sans < 150:
                            x_sans += kier_s_x * czas
                            porusz_sans = 0
                        else:
                            porusz_sans = 1
                            kier_s_x = 0
                            licznik_ataku = 0
                            a = a1
                            cz2_a = True

                ### HIT OR MISS? ###
                if cz2_a:
                    if not ply:
                        hit.play()
                        ply = True
                    licznik_cz2_a += 1
                    if licznik_cz2_a > oczekiwanie1:
                        okienko.blit(devil,(215,41))
                        if licznik_cz2_a > oczekiwanie1*2:
                            okienko.blit(hitormiss,(248,92))
                            if licznik_cz2_a > oczekiwanie1*3:
                                okienko.blit(iguess,(285,193))
                                if licznik_cz2_a > oczekiwanie1*4:
                                    okienko.blit(huh,(350,324))
                                if licznik_cz2_a > oczekiwanie1*24:
                                    licznik_cz2_a = 0
                                    atak = 0
                                    cz2_a = False
                                    czas_rundy = 0
                                    kier_x = 0.2
                                    kier_y = 0.2
                                    kier_k_x = 0.3
                                    kier_k_y = 0.2
                                    ply = False
                                    ile_atk += 1

            ### ITEMY ###
            if itemek:

                iterator = 0
                to_pop = False
                if not use:
                    x = 368
                    y = 560
                    for item in eq:
                        wys_item = list(pos_nazw[iterator])[1]
                        y_item = list(pos_nazw[iterator])[0]
                        name = u"· " + item[0]
                        wielkosc = font.getsize(name)
                        if list(pos)[0] > y_item and list(pos)[0] < y_item + list(wielkosc)[0] and list(pos)[1] > wys_item and list(pos)[1] < wys_item + list(wielkosc)[1]:
                            nazwa = czcionka.render(name,True,zolty)
                            if pygame.mouse.get_pressed()[0] and not use:
                                use = True
                                using = iterator
                                to_pop = iterator + 1
                        else:
                            nazwa = czcionka.render(name,True,biay)
                        okienko.blit(nazwa,pos_nazw[iterator])
                        iterator += 1
                    if to_pop:
                        uzywany_item = eq[using]
                        eq.pop(to_pop - 1)
                        to_pop = False
                        kier_x = 0.2
                        kier_y = 0.2
                        kier_k_x = 0.3
                        kier_k_y = 0.2
                else:
                    x = 550
                    y = 560
                    if uzywany_item[2] == "HP":
                        if not dodane:
                            rzydzie += uzywany_item[1] * 100
                            if rzydzie > 10000:
                                rzydzie = 10000
                            dodane = True
                        if licznik_INT < czas_INT:
                            ITM1 = czcionka.render(u"Użyłeś " + uzywany_item[0],True,biay)
                            ITM2 = czcionka.render(u"Uleczenie o: " + str(uzywany_item[1]),True,biay)
                            okienko.blit(ITM1,(130, 520))
                            okienko.blit(ITM2,(130, 570))
                            licznik_INT += 1
                        else:
                            mozna = True
                    else:
                        if uzywany_item[2] == "ATK":
                            if licznik_INT < czas_INT:
                                ITM1 = czcionka.render(u"Użyłeś " + uzywany_item[0],True,biay)
                                okienko.blit(ITM1,(130, 520))
                                if uzywany_item[0] == "Bullet":
                                    ITM2 = czcionka.render(u"Bullets don't work Jon",True,biay)
                                    okienko.blit(ITM2,(130,570))
                                else:
                                    if not zmniejszone:
                                        losu = random.randint(0,1)
                                        if losu == 0:
                                            kier_x = 0.1
                                            kier_y = 0.1
                                            string = "A to pech!"
                                            zmniejszone = True
                                        else:
                                            kier_k_x = 0.15
                                            kier_k_y = 0.1
                                            string = "Farcik!"
                                            zmniejszone = True
                                    ITM2 = czcionka.render(u"Spowolnionko! " + string,True,biay)
                                    okienko.blit(ITM2,(130,570))
                                licznik_INT += 1
                            else:
                                mozna = True
                    if mozna:
                        itemek = 0
                        use = False
                        using = False
                        czas_rundy = 0
                        licznik_INT = 0
                        mozna = False
                        zmniejszone = False
                        dodane = False
        ### ZAKONCZENIE ###
        else:
            if not ile_atk == ilosc_rund - 1:
                okienko.blit(victory,(0,0))
                pygame.mixer.music.stop()
                pygame.mixer.music.load("res/victory_royale.mp3")
                pygame.mixer.music.play()
                pygame.display.update()
                lew = False
                pra = False
                gor = False
                dol = False
                koniec()
                pygame.mixer.music.stop()
                pygame.mixer.music.load("res/muzyka.mp3")
                pygame.mixer.music.play()
                rzydzie = 10000
                czas_rundy = 0
                licznik_rund = 0
                kier_x = 0.2
                kier_y = 0.2
                x = 200
                y = 560
                kier_k_x = 0.3
                kier_k_y = 0.2
                kosci1 = []
                kosci2 = []
                kosci3 = []
                eq = [[u"LÖÖPS",20, "HP"],[u"Ślimor",42069, "ATK"],["Bitch Lasagna",40, "HP"],["Bullet",1,"ATK"]]
                ile_atk = 0
                endless = False
            else:
                endless = True
                unlock_endless = True


    ### BAD TOM ###
    if list(pos)[0] > 454 and list(pos)[0] < 507 and list(pos)[1] > 463 and list(pos)[1] < 484:
        if pygame.mouse.get_pressed()[0]:
            badtom = 1

    if badtom and licznik_tom < 500:
        if licznik_tom < 100:
            okienko.blit(tom,(x_tom,y_tom))
        if licznik_tom > 150 and licznik_tom < 200:
            okienko.blit(tom,(x_tom,y_tom))
        if licznik_tom > 250 and licznik_tom < 300:
            okienko.blit(tom,(x_tom,y_tom))
        if licznik_tom > 320 and licznik_tom < 340:
            okienko.blit(tom,(x_tom,y_tom))
        if licznik_tom > 360 and licznik_tom < 380:
            okienko.blit(tom,(x_tom,y_tom))
        if licznik_tom > 400 and licznik_tom < 420:
            okienko.blit(tom,(x_tom,y_tom))
        if licznik_tom > 430 and licznik_tom < 440:
            okienko.blit(tom,(x_tom,y_tom))
        if licznik_tom > 450 and licznik_tom < 460:
            okienko.blit(tom,(x_tom,y_tom))
        if licznik_tom > 470 and licznik_tom < 480:
            okienko.blit(tom,(x_tom,y_tom))
    else:
        licznik_tom = 0
        badtom = 0

    ### LICZNIKI ###
    i += 1
    j += 1
    licznik_tom += 1

    ### �YCIE ###
    pygame.draw.rect(okienko,szary,(328,698,154,49))
    pygame.draw.rect(okienko,RED,(330,700,150 * (rzydzie//100)/100,45))
    okienko.blit(rzycie,(350,700))
    ile = czcionka.render(str(rzydzie//100),True,biay)
    okienko.blit(ile,(420,700))

    ### RUNDY ###
    if not endless:
        nap = czcionka.render("Runda: " + str(licznik_rund +1 ) + "/" + str(ilosc_rund),True,biay)
        okienko.blit(nap,(0,0))
    else:
        nap = czcionka.render("Runda: " + str(licznik_rund),True,biay)
        endless_napis = czcionka.render("ENDLESS MODE ACTIVATED",True,RED)
        okienko.blit(endless_napis,(355,750))
        okienko.blit(nap,(0,0))
    
    pygame.display.update()

pygame.quit()
