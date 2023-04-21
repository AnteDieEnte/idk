import pygame
import sys
import os
import ctypes
import math
from pygame.locals import *


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

ctypes.windll.user32.SetProcessDPIAware()
WHITE = (255,255,255)
ORANGE = (255, 127, 80)
f = 1
w = 600
h = 600
OC = Zielcon = dict()
SP = dict()
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
screen = pygame.display.set_mode(([w*f,h*f]), pygame.RESIZABLE)
clock = pygame.time.Clock()
mosoff = 0
def u(x):
    global Xoffset,f
    x = (x*60)*f+Xoffset
    return x

def r(y):
    global Yoffset,f
    y = (y*60)*f+Yoffset
    return y

x = 0
blen = 0
Xoffset = 0
Yoffset = 0
breite = 56 * f + 4 * f
hohe = 56 * f + 4 * f
checkX = 0
checkY = 0
currentlvl = prevlvl = levels = 0
levelspage = currentpage = 0
settingswin = 2
hold = 0

OZeit = LZeit = UZeit = RZeit = 0
# sprungvar = -16
moves = 0

settings = pygame.image.load('pause.png').convert_alpha()
slider = pygame.image.load('slider.png').convert_alpha()
settingsrad = pygame.image.load('rad.png').convert_alpha()
musicpic = pygame.image.load('Music.png').convert_alpha()
soundpic = pygame.image.load('SoundTHICC.png').convert_alpha()
circleslider = pygame.image.load('Kreis.png').convert_alpha()
respic = pygame.image.load("reset2.png").convert_alpha()
homepic = pygame.image.load("home6.png").convert_alpha()
playpic = pygame.image.load("play.png").convert_alpha()
levelspic = pygame.image.load("levels.png").convert_alpha()
levelsrect = pygame.image.load("rectlevels.png").convert_alpha()
pfeilpic = pygame.image.load("pfeil.png").convert_alpha()
kreispic = pygame.image.load("Kreis.png").convert_alpha()

playpic.set_alpha(0)
levelspic.set_alpha(0)
settingsrad.set_alpha(0)

circleslider.set_alpha(130)
alphasettings = 200
zoomf = 1
alphabackground = alphabackground2 = 0
Clock = 0
start = 0
RED = (255,255,0)
color = dict()
color[0] = (255,0,0) #red
color[1] = (0, 113, 255)#(0,128,255) #blue
color[2] = (245, 151, 236) #pink
color[3] = (145, 83, 190) # violet
color[4] = (0, 201, 240)#(64, 197, 219) # light blue
color[5] = (22, 172, 18) #(0,128,0) #green
color[6] = (237, 232, 26) # yellow
color[7] = (252, 91, 0)#(255, 142, 1) # orange
color[8] = (0, 184, 124) #(14, 222, 159) # teal
color[9] = (139, 26, 26) #dark red



esckey = rkey = 0
move_sound = pygame.mixer.Sound('Memo-003.wav')
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)
def window():
    global Xoffset, Yoffset, f, breite, hohe, speed, x, y, checkX, checkY, w, h, b, t, b1, t1
    breite = 56 * f + 4 * f
    hohe = 56 * f + 4 * f
    w, h = pygame.display.get_surface().get_size()
    if not checkX == w or not checkY == h:
        if w > h:
            Yoffset = 0
            Xoffset = (w/2)-h/2
            f = h/600
        if h > w:
            Xoffset = 0
            Yoffset = (h/2)-w/2
            f = w/600
        if h==w:
            Xoffset = 0
            Yoffset = 0
            f = w/600
    checkX = w
    checkY = h
    screen.fill((255,127,80))

#def lvl(ZielSPX, ZielSPY, lol):
#    global ZielSP, ZielSP1, color, b, t, SP
#    #Ziel


    #Spieler

    #if MC[1](ZielSP1):
    #    pygame.draw.rect(screen, (86, 255, 60), (ZielSP1X + 15 * f, ZielSP1Y + 15 * f, breite / 2, hohe / 2))
    #else:
    #    pygame.draw.rect(screen, (0,128,255), (ZielSP1X + 15 * f, ZielSP1Y + 15 * f, breite / 2, hohe / 2))


def linien():
    #wagerecht
    for bruh in range(int(60), int(600), int(60)):
        pygame.draw.rect(screen, (100, 100, 100), (0+Xoffset, (bruh-2)*f+Yoffset,600*f,4*f))
    #senkrecht
    for bruh in range(60, 600, 60):
        pygame.draw.rect(screen, (100, 100, 100), ((bruh-2)*f+Xoffset,0+Yoffset,4*f,600*f))

def außenlinien():

    pygame.draw.rect(screen, (0, 0, 0), (-998*f+Xoffset,  0+Yoffset,  1000*f,  600*f))#links
    pygame.draw.rect(screen, (0, 0, 0), ((600-2)*f+Xoffset,  0+Yoffset,  1000*f,  600*f))#rechts
    pygame.draw.rect(screen, (0, 0, 0), (0+Xoffset,  -998*f+Yoffset,  600*f,  1000*f))#oben
    pygame.draw.rect(screen, (0, 0, 0), (0+Xoffset,  (600-2)*f+Yoffset,  600*f,  1000*f))#

def hitbox():
    global SP, b, t, tt, blen
    for x in range(blen):
        s = list(tt)[x]
        SP[s] = pygame.Rect(u(b[s]),r(t[s]), breite, hohe)
        SP["l"+str(s)] = Rect(u(b[s]-1),r(t[s]),breite,hohe)
        SP["r"+str(s)] = Rect(u(b[s]+1),r(t[s]),breite,hohe)
        SP["u"+str(s)] = Rect(u(b[s]),r(t[s]+1),breite,hohe)
        SP["o"+str(s)] = Rect(u(b[s]),r(t[s]-1),breite,hohe)


def windowpause():
    settingsrect = pygame.Surface((w, h))
    settingsrect.fill((255, 255, 255))
    pygame.Surface.set_alpha(settingsrect, alphabackground)
    screen.blit(settingsrect, (0, 0))
    #print(zoomf)
    settingsrect = pygame.Surface((500 * zoomf * f, 336 * zoomf * f))
    screen_rect = screen.get_rect()
    text_rect = settingsrect.get_rect(center=screen_rect.center)
    settingsrect.fill(ORANGE)
    pygame.Surface.set_alpha(settingsrect, 235)
    screen.blit(settingsrect, (text_rect))

def settingspause():
    global musicpos, soundpos, mosoff, prevmusic, prevsound, hold, prevmusic, prevsound, reslvl, settingswin, home, true
    true = False
    slider1 = pygame.transform.smoothscale(slider, (350 * f * zoomf, 30 * f * zoomf))
    slider1.set_alpha (170)
    screen.blit(slider1, (w / 2 - 140 * f * zoomf, h / 2 + 5 * f * zoomf))
    screen.blit(slider1, (w / 2 - 140 * f * zoomf, h / 2 - 55 * f * zoomf))
    circleslider1 = pygame.transform.smoothscale(circleslider, (36* f * zoomf,36* f * zoomf))
    circleslider2 = pygame.transform.smoothscale(circleslider, (36* f * zoomf,36* f * zoomf))

    musicpic.set_alpha(50+musicpos*120)
    soundpic.set_alpha(50+soundpos*120)

    musicpic1 = pygame.transform.smoothscale(musicpic, (36 * f * zoomf, 36 * f * zoomf))
    soundpic1 = pygame.transform.smoothscale(soundpic, (36 * f * zoomf, 36 * f * zoomf))

    s = 60*zoomf*f
    homepic1 = pygame.transform.smoothscale(homepic, (s,s))
    respic1 = pygame.transform.smoothscale(respic, (s,s))
    playpic1 = pygame.transform.smoothscale(playpic, (s,s))
    print(homepic1.get_rect())

    a1 = pygame.Rect((w / 2 - 180 * f, h / 2 + 70 * f), (s,s))
    a2 = pygame.Rect((w / 2 - 30 * f, h / 2 + 70 * f), (s,s))
    a3 = pygame.Rect((w / 2 + 120 * f, h / 2 + 70 * f), (s,s))

    font = pygame.font.Font(resource_path('ROGFonts-Regular.ttf'), int(30 * zoomf * f))

    level = font.render("Level: " + str(currentlvl), True, (255, 255, 255))
    text_rect = level.get_rect(center=(w/2, h/2 - 130*zoomf*f))
    level.set_alpha(200)
    screen.blit(level, (text_rect))

    if math.sqrt(pow((175+musicpos*320)*f +u(0) - mosx, 2) + pow(260*f - mosy +r(0), 2)) <= 18*f or mosoff == 2:
        if pygame.mouse.get_pressed()[0] == 0:
            mosoff = 2
            circleslider1.set_alpha(170)
        if mosoff == 2 and pygame.mouse.get_pressed()[0] == 1:
            circleslider1.set_alpha(200)
            i = (mosx - 175*f- u(0))/(320*f)
            #print(i)
            if i > 1:
                i = 1
            if i < 0:
                i = 0
            pygame.mixer.music.set_volume(i)
            musicpos = pygame.mixer.music.get_volume()

    if math.sqrt(pow((175+soundpos*320)*f - mosx +u(0), 2) + pow(320*f - mosy+r(0), 2)) <= 18*f or mosoff == 3:
        if pygame.mouse.get_pressed()[0] == 0:
            mosoff = 3
            circleslider2.set_alpha(170)
        if mosoff == 3 and pygame.mouse.get_pressed()[0] == 1:
            circleslider2.set_alpha(200)
            i = (mosx - 175*f -u(0))/(320*f)
            #print(i)
            if i > 1:
                i = 1
            if i < 0:
                i = 0
            move_sound.set_volume(i)
            soundpos = move_sound.get_volume()

    #print(mosoff)
    if not math.sqrt(pow((175+musicpos*320)*f +u(0) - mosx, 2) + pow(260*f - mosy +r(0), 2)) <= 18*f and\
       not math.sqrt(pow((175+soundpos*320)*f - mosx +u(0), 2) + pow(320*f - mosy+r(0), 2)) <= 18*f\
            and pygame.mouse.get_pressed()[0] == 0 and (mosoff == 2 or mosoff == 3):
            mosoff = 0
            if musicpos != 0: prevmusic = musicpos
            if soundpos != 0: prevsound = soundpos


    screen.blit(circleslider2, (w / 2 + (soundpos*320 - 143) * f * zoomf, h / 2 + 2 * f * zoomf))
    screen.blit(circleslider1, (w / 2 + (musicpos*320 - 143) * f * zoomf, h / 2 - 58 * f * zoomf))


    ### settings buttons ###
    Mosx = mosx - u(0)
    Mosy = mosy - r(0)

    #music
    if hold == 4:
        if not pygame.mouse.get_pressed()[0] == 1:
            hold = 0
            if musicpos == 0:
                try:
                    pygame.mixer.music.set_volume(prevmusic)
                    musicpos = prevmusic
                except:
                    pygame.mixer.music.set_volume(1.0)
                    musicpos = 1.0
            elif musicpos != 0:
                pygame.mixer.music.set_volume(0)
                musicpos = 0
    if 100 * f < Mosx < 136 * f and 242 * f < Mosy < 278 * f and not pygame.mouse.get_pressed()[0] == 1 and drucken != 0:
        mosoff = 4
        musicpic1.set_alpha(90 + musicpos * 120)
    if (not 100 * f < Mosx < 136 * f and not 242 * f < Mosy < 278 * f) and mosoff == 4:
        mosoff = 0
        hold = 0
    if 100 * f < Mosx < 136 * f and 242 * f < Mosy < 278 * f and \
            (pygame.mouse.get_pressed()[0] == 1 and mosoff == 4):
        hold = 4
        musicpic1.set_alpha(135 + musicpos * 120)

    #sound
    if hold == 5:
        if not pygame.mouse.get_pressed()[0] == 1:
            hold = 0
            if soundpos == 0:
                try:
                    pygame.mixer.music.set_volume(prevsound)
                    soundpos = prevsound
                except:
                    pygame.mixer.music.set_volume(1.0)
                    soundpos = 1.0
            elif soundpos != 0:
                pygame.mixer.music.set_volume(0)
                soundpos = 0
    if 100*f < Mosx < 136 * f and 302*f < Mosy < 338*f and not pygame.mouse.get_pressed()[0] == 1 and drucken != 0:
        mosoff = 5
        soundpic1.set_alpha(90 + soundpos * 120)
    if (not 100*f < Mosx < 136 * f or not 302*f < Mosy < 338*f) and mosoff == 5:
        mosoff = 0
        hold = 0
    if 100*f < Mosx < 136 * f and 302*f < Mosy < 338*f and\
    (pygame.mouse.get_pressed()[0] == 1 and mosoff == 5):
        hold = 5
        soundpic1.set_alpha(135 + soundpos * 120)

    screen.blit(musicpic1, (w / 2 - 200 * f * zoomf, h / 2 - 58 * f * zoomf))
    screen.blit(soundpic1, (w / 2 - 200 * f * zoomf, h / 2 + 2 * f * zoomf))

    colliderect(a3,playpic1,7)
    if true == True:
        settingswin = 0

    colliderect(a2,respic1,6)
    if true == True:
        reslvl = 1

    colliderect(a1, homepic1,8)
    if true == True:
        home = 2
        reslvl = 1




    screen.blit(homepic1, (w / 2 - 180 * f * zoomf, h / 2 + 70 * f * zoomf))
    screen.blit(respic1, (w / 2 - 30 * f * zoomf, h / 2 + 70 * f * zoomf))
    screen.blit(playpic1, (w / 2 + 120 * f * zoomf, h / 2 + 70 * f * zoomf))

def colliderect(a, rect, msoffhold):
    global hold, mosoff, true
    true = False
    if hold == msoffhold:
        if not pygame.mouse.get_pressed()[0] == 1:
            hold = 0
            true = True
    if mouserect.colliderect(a) and \
            (pygame.mouse.get_pressed()[0] == 1 and mosoff == msoffhold):
        hold = msoffhold
        pygame.Surface.set_alpha(rect, 225)
    elif mouserect.colliderect(a) and not pygame.mouse.get_pressed()[0] == 1 and drucken != 0:
        mosoff = msoffhold
        pygame.Surface.set_alpha(rect, 210)
    else:
        pygame.Surface.set_alpha(rect, 170)
        if mosoff == msoffhold:
            mosoff = 0
            hold = 0

def levelsblit(extralevels, extrapos, lol3):
    global alphabackground, drucken, home, prevlvl
    for x in range(-1, 5):
        levelsrect1.set_alpha(0)
        if lol3 == 0:
            if x < 2:
                aa[x] = Rect((w / 2 +( 180 * x - 80 )*f, h/2 -170*f+lol3 * 1000 + extrapos),(160*f, 160*f), border_radius=25*f)
            else:
                aa[x] = Rect((w / 2 + ( 180 * (x-3) - 80 )*f, h/2 + 10*f+lol3 * 1000 + extrapos),(160*f, 160*f), border_radius=25*f)
        else:
            aa[x] = Rect((0,0),(0,0))
        colliderect(aa[x], levelsrect1, x + 10)
        if true:
            prevlvl = x + 1 + extralevels
            alphabackground = 4.1
            drucken = 0
        if x < 2:
            aa[x] = screen.blit(levelsrect1, (w / 2 +( 180 * x + lol3 * 150 + extrapos- 80 )*f, h/2 -170*f))
        else:
            aa[x] = screen.blit(levelsrect1, (w / 2 + ( 180 * (x-3) + lol3 * 150 + extrapos- 80 )*f, h/2 + 10*f ))
        level = font.render(str(x + 2 + extralevels), True, (ORANGE))
        text_rect = level.get_rect(center=aa[x].center)
        screen.blit(level, (text_rect))


def boxcollide(CR):
    global Box, SP, tt
    for x in range(len(Box)):
        if CR.colliderect(Box[x+1]):
            return False

    for x in range(len(tt)):
        if CR.colliderect(SP[list(tt)[x]]):
            return False
    return True

def sheesh():
    global settingsrect, alphabackground
    pygame.Surface.set_alpha(settingsrect, alphabackground)
    screen.blit(settingsrect, (0, 0))




titlescreen = go = True

#[links,rechts,stand,sprung]
s = 0
currentlvl = 0
reslvl = 0
neulvl = 0
stop = 1
drucken = -2
wait = 0
printlevel = 1
while titlescreen:
    print(clock.get_fps())
    window()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    if pygame.time.get_ticks() > 1000:
        font = pygame.font.Font(resource_path('ROGFonts-Regular.ttf'), int(50 * f * zoomf))
        fontgroß = pygame.font.Font(resource_path('ROGFonts-Regular.ttf'), int(120 * f * zoomf))
        red = fontgroß.render("Red", True, (255, 0, 0))
        #(0,128,255)
        friend = font.render("and a friend", True, (255, 255, 255))

        text_rect = red.get_rect(center=(w / 2, h / 2 - (75 + s) * zoomf * f))
        text_rect1 = friend.get_rect(center=(w / 2, h / 2 + (15 - s) * zoomf * f))

        if pygame.time.get_ticks() > 4000:
            if s < 50:
                s += 1.5
            else:
                titlescreen = False
                zoomf = 0
                home = 1
        else:
            if alphabackground < 255:
                alphabackground += 2
            else:
                alphabackground = 255




        red.set_alpha(alphabackground)
        friend.set_alpha(alphabackground)
        screen.blit(red, (text_rect))
        screen.blit(friend, (text_rect1))

    pygame.display.update()
    clock.tick(60)
    print(titlescreen)

lol = lol2 = lol3 = lolturn = 0

alphabackground = 0
b = t = dict()
start = -2
while go:
    print(clock.get_fps())
    while home == 1:
        print(clock.get_fps())
        mosx, mosy = pygame.mouse.get_pos()
        mouserect = pygame.draw.rect(screen, (0, 0, 0), (mosx, mosy, 1, 1), 0)
        window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        fontklein = pygame.font.Font(resource_path('ROGFonts-Regular.ttf'), int(20 * f))
        font = pygame.font.Font(resource_path('ROGFonts-Regular.ttf'), int(50 * f))
        fontgroß = pygame.font.Font(resource_path('ROGFonts-Regular.ttf'), int(120 * f))
        if start % 2 == 0:
            red = fontgroß.render("Red", True, (255, 0, 0))
            # (0,128,255)
            friend = font.render("and a friend", True, (255, 255, 255))

            text_rect = red.get_rect(center=(w / 2, h / 2 - 126 * f))
            text_rect1 = friend.get_rect(center=(w / 2, h / 2 - 36 * f))

            red.set_alpha(255)
            friend.set_alpha(255)
            screen.blit(red, (text_rect))
            screen.blit(friend, (text_rect1))

        s = 80 * f
        levelspic1 = pygame.transform.smoothscale(levelspic, (s, s))
        playpic1 = pygame.transform.smoothscale(playpic, (s, s))
        settingsrad1 = pygame.transform.smoothscale(settingsrad, (s, s))

        a1 = pygame.Rect((w / 2 - 240 * f, h / 2 + 70 * f), (s,s))
        a2 = pygame.Rect((w / 2 - 40 * f, h / 2 + 70 * f), (s,s))
        a3 = pygame.Rect((w / 2 + 160 * f, h / 2 + 70 * f), (s,s))
        # replay

        if start == 5:
            homepic1 = pygame.transform.smoothscale(homepic, (60*f, 60*f))
            a1 = pygame.Rect((u(0)+40*f, r(0)+50*f), (60*f,60*f), border_radius=15)
            colliderect(a1, homepic1, 8)
            if true == True:
                alphabackground = 3.1
            screen.blit(homepic1, (u(0)+40*f, r(0)+50*f))

            aa = dict()
            s = 160*f
            levelsrect1 = pygame.transform.smoothscale(levelsrect, (s, s))
            kreispic1 = pygame.transform.smoothscale(kreispic, (30 * f, 30 * f))
            for x in range (-1,2):
                aa[x] = Rect((w/2 +(x*50-15)*f, h/2+(200-15)*f), (30*f, 30*f), border_radius=15)
                colliderect(aa[x], kreispic1, x + 20)
                if true:
                    levelspage = x + 2
                    if currentpage != levelspage:
                        if w/h >= 1.5:
                            big = w
                        else:
                            big = w*1.5
                        big = big * abs(currentpage - levelspage)
                        sqrtf =math.sqrt(big/300)
                        sqrtfr = round(sqrtf,1)

                screen.blit(kreispic1, (w/2 +(x*50-15)*f, h/2+(200-15)*f))
                if levelspage != x + 2:
                    pygame.draw.circle(screen, (ORANGE), (w/2 +(x*50)*f, h/2+(200)*f), 10*f)
            if currentpage != levelspage:
                if lolturn == 1:
                    if round(lol,4) == 0:
                        lolturn = 2
                    else:
                        lol -= 0.1
                        lol2 += (lol+0.1)*(lol+0.1)-lol*lol
                else:
                    lol += 0.1
                    if round(lol,4) == sqrtfr:
                        lol = sqrtfr
                        lolturn = 1
                    lol2 = round(lol * lol, 4)
                if currentpage < levelspage:
                    lol3 = lol2 * (-1)
                    lol4 = 1
                else:
                    lol3 = lol2
                    lol4 = -1
                for x in range(abs(currentpage - levelspage)+1):
                    if lol4 == 1:
                        extralevels = (currentpage-1+x)*6
                    else:
                        extralevels = (currentpage- 1 - x) * 6
                    extrapos = ((x*lol4)*sqrtfr*sqrtfr*300)/abs(currentpage - levelspage)
                    levelsblit(extralevels, extrapos, lol3)
                if lolturn == 2:
                    currentpage = levelspage
                    lolturn = 0
                extralevels = extrapos = 0
            else:
                levelsblit((levelspage-1)*6,0,0)




        if start == -4:
            alphabackground -=5
            settingsrect = pygame.Surface((w, h))
            settingsrect.fill(ORANGE)
            pygame.Surface.set_alpha(settingsrect, alphabackground)
            if alphabackground < 0:
                drucken = -1
                start = -2
                alphabackground = 0

        if drucken == -2:
            alphabackground += 2
            playpic1.set_alpha(alphabackground)
            levelspic1.set_alpha(alphabackground)
            settingsrad1.set_alpha(alphabackground)
            if alphabackground == 170:
                drucken = -1
                alphabackground = 0

        if (drucken == -1 or drucken == 0) and start % 2 == 0:
            colliderect(a3, playpic1, 7)
            if true == True:
                alphabackground = 3.1
                start = 0
                drucken = 0

            colliderect(a2, levelspic1, 6)
            if true == True:
                start = 4
                currentpage = levelspage = 1
                alphabackground = 3.1
                drucken = 0

            colliderect(a1, settingsrad1, 5)
            if true == True:
                pass

        if start >= 0 and alphabackground > 0:

            if alphabackground == 254.1:
                alphabackground = 255
                home = 0
                start = 1
            if alphabackground > 255:
                start += 1
                alphabackground = 258
                if start == 1:
                    home = 0
                drucken = 0
            if alphabackground % 3 != 0:
                alphabackground += 5
            else:
                alphabackground -= 3
            if alphabackground == 0:
                if start % 2 != 0:
                    drucken = 1
                else:
                    drucken = -1
            settingsrect = pygame.Surface((w, h))
            settingsrect.fill(ORANGE)
            pygame.Surface.set_alpha(settingsrect, alphabackground)




        screen.blit(settingsrad1, (w / 2 - 240 * f, h / 2 + 70 * f))
        screen.blit(levelspic1, (w / 2 - 40 * f, h / 2 + 70 * f))
        screen.blit(playpic1, (w / 2 + 160 * f, h / 2 + 70 * f))
        try:
            screen.blit(settingsrect, (0, 0))
        except:
            pass
        Clock += 1
        pygame.display.update()
        clock.tick(60)
    #print(clock.get_fps())
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    mosx, mosy = pygame.mouse.get_pos()
    mosfocused = pygame.mouse.get_focused()
    # print(mosx,mosy, mosfocused)
    mouserect = pygame.draw.rect(screen, (0, 0, 0), (mosx, mosy, 1, 1), 0)
    #try:
    #    SP = pygame.Rect(u(b),r(t),breite,hohe)
    #    SP1 = pygame.Rect(u(b1), r(t1), breite, hohe)
    #except:
    #    pass
    gedruckt = pygame.key.get_pressed()
    linkeWand = pygame.draw.rect(screen, (0, 0, 0), (-40 * f+Xoffset, 0+Yoffset, 80 * f, 600 * f), )
    rechteWand = pygame.draw.rect(screen, (0, 0, 0), (560 * f+Xoffset, 0+Yoffset, 80 * f, 600 * f), )
    obereWand = pygame.draw.rect(screen, (0, 0, 0), (0+Xoffset, -40 * f+Yoffset, 600 * f, 80 * f), )
    untereWand = pygame.draw.rect(screen, (0, 0, 0), (0+Xoffset, 560 * f+Yoffset, 600 * f, 80 * f), )


    if stop == 0:
        if currentlvl == 3:
            b[0] = 1
            t[0] = 0
            b[1] = 4
            t[1] = 0
        elif currentlvl == 10:
            b[0] = 9
            t[0] = 0
            b[1] = 0
            t[1] = 9
        elif currentlvl == 2:
            b[0] = 0
            t[0] = 9
            b[1] = 9
            t[1] = 9
        elif currentlvl == 1:
            b[0] = 0
            t[0] = 4
            b[1] = 0
            t[1] = 5
        elif currentlvl == 7:
            b[0] = 3
            t[0] = 6
            b[1] = 8
            t[1] = 8
        elif currentlvl == 5:
            b[0] = 0
            t[0] = 9
            b[1] = 9
            t[1] = 3
        elif currentlvl == 8:
            b[0] = 0
            t[0] = 0
            b[1] = 9
            t[1] = 9
        elif currentlvl == 9:
            b[0] = 5
            t[0] = 9
            b[1] = 4
            t[1] = 9
        elif currentlvl == 4:
            b[0] = 0
            t[0] = 6
            b[1] = 9
            t[1] = 3
        elif currentlvl == 6:
            b[0] = 6
            t[0] = 2
            b[1] = 6
            t[1] = 7
        elif currentlvl == 11:
            b[0] = 9
            t[0] = 7
            b[1] = 0
            t[1] = 2
        elif currentlvl == 12:
            b[0] = 3
            t[0] = 3
            b[1] = 6
            t[1] = 3
            b[2] = 3
            t[2] = 6
            b[3] = 6
            t[3] = 6
        elif currentlvl == 13:
            b[0] = 1
            t[0] = 1
            b[1] = 2
            t[1] = 2
        elif currentlvl == 14:
            b[0] = 1
            b[1] = 7
            b[2] = 9
            b[3] = 8
            b[4] = 6
            b[5] = 4
            b[6] = 3
            b[7] = 2
            b[8] = 5
            b[9] = 0
            t[0] = t[1] = t[2] = t[3] = t[4] = t[5] = t[6] = t[7] = t[8] = t[9] = 8
        elif currentlvl == 15:
            b[0] = 4
            t[0] = 0
            b[1] = 4
            t[1] = 9
            b[2] = 5
            t[2] = 0
            b[3] = 5
            t[3] = 9
        SP = dict()
        blen = len(b)
        tt = dict(sorted(t.items(), key=lambda x: x[1]))
        bb = dict(sorted(b.items(), key=lambda x: x[1]))
        hitbox()
        stop = 1


    if not gedruckt[pygame.K_UP]:
        OZeit = 0
    if not gedruckt[pygame.K_DOWN]:
        UZeit = 0
    if not gedruckt[pygame.K_LEFT]:
        LZeit = 0
    if not gedruckt[pygame.K_RIGHT]:
        RZeit = 0
    if drucken == 1:
        pb = dict(b)
        pt = dict(t)
        tt = dict(sorted(t.items(), key=lambda x: x[1]))
        bb = dict(sorted(b.items(), key=lambda x: x[1]))


        if gedruckt[pygame.K_UP] and not gedruckt[pygame.K_DOWN] and Clock > OZeit + 12:
            for x in range(blen):
                s = list(tt)[x]
                if not SP[s].colliderect(obereWand) and boxcollide(SP["o"+str(s)]):
                    t[s] -= 1
                hitbox()
            OZeit = Clock

        if gedruckt[pygame.K_DOWN] and not gedruckt[pygame.K_UP] and Clock > UZeit + 12:
            for x in range(blen):
                s = list(reversed(tt))[x]
                if not SP[s].colliderect(untereWand) and boxcollide(SP["u"+str(s)]):
                    t[s] += 1
                hitbox()
            UZeit = Clock

        if gedruckt[pygame.K_LEFT] and not gedruckt[pygame.K_RIGHT] and Clock > LZeit + 12:
            for x in range(blen):
                s = list(bb)[x]
                if not SP[s].colliderect(linkeWand) and boxcollide(SP["l"+str(s)]):
                    b[s] -= 1
                hitbox()
            LZeit = Clock



        if gedruckt[pygame.K_RIGHT] and not gedruckt[pygame.K_LEFT] and Clock > RZeit + 12:
            for x in range(blen):
                s = list(reversed(bb))[x]
                if not SP[s].colliderect(rechteWand) and boxcollide(SP["r"+str(s)]):
                    b[s] += 1
                hitbox()
            RZeit = Clock
        if pb != b:
            moves += 1
        if pt != t:
            moves += 1
        if pt != t or pb != b:
            move_sound.play()
        print(bb)



    window()
    draw = pygame.draw.rect
    Box = dict()
    if currentlvl == 3:
        Box[1] = draw(screen, (0,0,0), (u(2), r(0), breite * 2, hohe * 4))
        Box[2] = draw(screen, (0,0,0), (u(6), r(6), breite * 2, hohe * 4))
        Zielcon = dict({"x0": u(8), "y0": r(9), "x1": u(5), "y1": r(9)})
    elif currentlvl == 10:
        Box[1] = draw(screen, (0,0,0), (u(1), r(1), breite * 1, hohe * 9))
        Box[2] = draw(screen, (0,0,0), (u(8), r(0), breite * 1, hohe * 9))
        Box[3] = draw(screen, (0,0,0), (u(1), r(1), breite * 6, hohe * 1))
        Box[4] = draw(screen, (0,0,0), (u(3), r(8), breite * 6, hohe * 1))
        Box[5] = draw(screen, (0,0,0), (u(3), r(3), breite * 1, hohe * 6))
        Box[6] = draw(screen, (0,0,0), (u(6), r(1), breite * 1, hohe * 6))
        Box[7] = draw(screen, (0,0,0), (u(4), r(3), breite * 1, hohe * 1))
        Box[8] = draw(screen, (0,0,0), (u(5), r(6), breite * 1, hohe * 1))
        Zielcon = dict({"x0": u(5), "y0": r(3), "x1": u(4), "y1": r(6)})
    elif currentlvl == 2:
        Box[1] = draw(screen, (0,0,0), (u(0), r(2), breite * 5, hohe * 1))
        Box[2] = draw(screen, (0,0,0), (u(7), r(0), breite * 2, hohe * 4))
        Box[3] = draw(screen, (0,0,0), (u(0), r(5), breite * 3, hohe * 2))
        Box[4] = draw(screen, (0,0,0), (u(2), r(7), breite * 1, hohe * 1))
        Box[5] = draw(screen, (0,0,0), (u(5), r(5), breite * 5, hohe * 1))
        Box[6] = draw(screen, (0,0,0), (u(7), r(7), breite * 2, hohe * 3))
        Zielcon = dict({"x0": u(9), "y0": r(0), "x1": u(0), "y1": r(1)})
    elif currentlvl == 1:
        Box[1] = draw(screen, (0, 0, 0), (u(0), r(0), breite * 10, hohe * 4))
        Box[2] = draw(screen, (0, 0, 0), (u(0), r(6), breite * 10, hohe * 4))
        Box[3] = draw(screen, (0, 0, 0), (u(3), r(4), breite * 1, hohe * 1))
        Box[4] = draw(screen, (0, 0, 0), (u(6), r(5), breite * 1, hohe * 1))
        Zielcon = dict({"x0": u(9), "y0": r(4), "x1": u(9), "y1": r(5)})
    elif currentlvl == 7:
        Box[1] = draw(screen, (0, 0, 0), (u(0), r(0), breite * 10, hohe * 1))
        Box[2] = draw(screen, (0, 0, 0), (u(0), r(0), breite * 1, hohe * 10))
        Box[3] = draw(screen, (0, 0, 0), (u(9), r(0), breite * 1, hohe * 10))
        Box[4] = draw(screen, (0, 0, 0), (u(0), r(9), breite * 10, hohe * 1))
        Box[5] = draw(screen, (0, 0, 0), (u(4), r(4), breite * 2, hohe * 2))
        Zielcon = dict({"x0": u(6), "y0": r(3), "x1": u(1), "y1": r(1)})
    elif currentlvl == 5:
        Box[1] = draw(screen, (0,0,0), (u(1), r(0), breite * 3, hohe * 2))
        Box[2] = draw(screen, (0,0,0), (u(6), r(8), breite * 4, hohe * 2))
        Box[3] = draw(screen, (0,0,0), (u(1), r(3), breite * 3, hohe * 6))
        Box[4] = draw(screen, (0,0,0), (u(6), r(1), breite * 3, hohe * 6))
        Box[5] = draw(screen, (0,0,0), (u(0), r(7), breite * 1, hohe * 2))
        Box[6] = draw(screen, (0,0,0), (u(9), r(1), breite * 1, hohe * 2))
        Zielcon = dict({"x0": u(9), "y0": r(0), "x1": u(0), "y1": r(0)})
    elif currentlvl == 8:
        Box[1] = draw(screen, (0,0,0), (u(0), r(5), breite * 10, hohe * 1))
        Box[2] = draw(screen, (0,0,0), (u(8), r(0), breite * 1, hohe * 1))
        Zielcon = dict({"x0": u(6), "y0": r(2), "x1": u(2), "y1": r(7)})
    elif currentlvl == 9:
        Box[1] = draw(screen, (0,0,0), (u(0), r(0), breite * 3, hohe * 10))
        Box[2] = draw(screen, (0,0,0), (u(7), r(0), breite * 3, hohe * 10))
        Box[3] = draw(screen, (0,0,0), (u(4), r(7), breite * 2, hohe * 2))
        Zielcon = dict({"x0": u(3), "y0": r(3), "x1": u(6), "y1": r(0)})
    elif currentlvl == 4:
        Box[1] = draw(screen, (0,0,0), (u(2),r(5),breite*2, hohe*2))
        Box[2] = draw(screen, (0,0,0), (u(6),r(3),breite*1, hohe*1))
        Box[3] = draw(screen, (0,0,0), (u(6),r(4),breite*2, hohe*1))
        Box[4] = draw(screen, (0,0,0), (u(0),r(0),breite*10, hohe*3))
        Box[5] = draw(screen, (0,0,0), (u(0),r(7),breite*10, hohe*3))
        Zielcon = dict({"x0": u(8), "y0": r(3), "x1": u(1), "y1": r(6)})
    elif currentlvl == 6:
        Box[1] = draw(screen, (0, 0, 0), (u(0), r(0), breite * 1, hohe * 10))
        Box[2] = draw(screen, (0, 0, 0), (u(9), r(0), breite * 1, hohe * 10))
        Box[3] = draw(screen, (0, 0, 0), (u(3), r(0), breite * 1, hohe * 2))
        Box[4] = draw(screen, (0, 0, 0), (u(3), r(3), breite * 1, hohe * 4))
        Box[5] = draw(screen, (0, 0, 0), (u(3), r(8), breite * 1, hohe * 2))
        Box[6] = draw(screen, (0, 0, 0), (u(0), r(0), breite * 10, hohe * 1))
        Box[7] = draw(screen, (0, 0, 0), (u(0), r(9), breite * 10, hohe * 1))
        Zielcon = dict({"x0": u(3), "y0": r(7), "x1": u(3), "y1": r(2)})
    elif currentlvl == 11:
        Box[1] = draw(screen, (0, 0, 0), (u(0), r(0), breite * 10, hohe * 1))
        Box[2] = draw(screen, (0, 0, 0), (u(0), r(1), breite * 9, hohe * 1))
        Box[3] = draw(screen, (0, 0, 0), (u(1), r(2), breite * 8, hohe * 1))
        Box[4] = draw(screen, (0, 0, 0), (u(4), r(4), breite * 2, hohe * 2))
        Box[5] = draw(screen, (0, 0, 0), (u(1), r(7), breite * 8, hohe * 1))
        Box[6] = draw(screen, (0, 0, 0), (u(1), r(8), breite * 9, hohe * 1))
        Box[7] = draw(screen, (0, 0, 0), (u(0), r(9), breite * 10, hohe * 1))
        Zielcon = dict({"x0": u(0), "y0": r(7), "x1": u(9), "y1": r(2)})
    elif currentlvl == 12:
        Box[1] = draw(screen, (0, 0, 0), (u(4), r(4), breite * 2, hohe * 2))
        Zielcon = dict({"x0": u(1), "y0": r(1), "x1": u(8), "y1": r(8),"x2": u(1), "y2": r(8), "x3": u(8), "y3": r(1)})
        if gedruckt[pygame.K_RIGHT]:
            #print(b[2], b[3])
            for x in range(3):
                if (b[x] - b[3]) != 1 or t[x] != t[3]:
                    b[x] = pb[x]
            #print(b[2], b[3])
        if gedruckt[K_LEFT]:
            #print(b[2], b[3])
            for x in range(3):
                if b[x] - b[3] != -1 or t[x] != t[3]:
                    b[x] = pb[x]
            #print(b[2], b[3])
        if gedruckt[K_DOWN]:
            #print(b[2], b[3])
            for x in range(3):
                if t[x] - t[3] != 1 or b[x] != b[3]:
                    t[x] = pt[x]
            #print(b[2], b[3])
        if gedruckt[K_UP]:
            #print(b[2], b[3])
            for x in range(3):
                if t[x] - t[3] != -1 or b[x] != b[3]:
                    t[x] = pt[x]
            #print(b[2], b[3])

        hitbox()



    elif currentlvl == 13:
        Box[1] = draw(screen, (0, 0, 0), (u(4), r(4), breite * 2, hohe * 2))
        if (moves+2)%2 == 0:
            Zielcon = dict({"x0": u(3), "y0": r(6), "x1": u(6), "y1": r(3)})
        else:
            Zielcon = dict({"x0": u(6), "y0": r(3), "x1": u(3), "y1": r(6)})
    elif currentlvl == 14:
        Box[1] = draw(screen, (0, 0, 0), (u(0), r(0), breite * 10, hohe * 1))
        Box[2] = draw(screen, (0, 0, 0), (u(4), r(4), breite * 2, hohe * 2))
        Box[3] = draw(screen, (0, 0, 0), (u(0), r(9), breite * 10, hohe * 1))
        Zielcon = dict({"x0": u(0), "y0": r(1), "x1": u(1), "y1": r(1), "x2": u(2), "y2": r(1), "x3": u(3), "y3": r(1), "x9": u(9), "y9": r(1),\
                    "x4": u(4), "y4": r(1), "x5": u(5), "y5": r(1), "x6": u(6), "y6": r(1),  "x7": u(7), "y7": r(1),  "x8": u(8), "y8": r(1)})
    elif currentlvl == 15:
        Box[1] = draw(screen, (0, 0, 0), (u(1), r(0), breite * 3, hohe * 3))
        Box[2] = draw(screen, (0, 0, 0), (u(1), r(7), breite * 3, hohe * 3))
        Box[3] = draw(screen, (0, 0, 0), (u(6), r(0), breite * 3, hohe * 3))
        Box[4] = draw(screen, (0, 0, 0), (u(6), r(7), breite * 3, hohe * 3))
        Zielcon = dict({"x0": u(2), "y0": r(3), "x1": u(2), "y1": r(6), "x2": u(7), "y2": r(3), "x3": u(7), "y3": r(6)})
    for x in range(blen):
        SP["Ziel" + str(x)] = pygame.draw.rect(screen, (86, 255, 60), (Zielcon["x"+str(x)], Zielcon["y"+str(x)], breite, hohe))
    for x in range(blen):
        pygame.draw.rect(screen, (color[x]), (u(b[x]), r(t[x]), breite, hohe))
    if drucken != 0: true = True

    for x in range(blen):
        if SP[x].colliderect(SP["Ziel"+str(x)]):
            pygame.draw.rect(screen, (86, 255, 60), (Zielcon["x"+str(x)] + 15 * f, Zielcon["y"+str(x)] + 15 * f, breite / 2, hohe / 2))
        else:
            pygame.draw.rect(screen, (color[x]), (Zielcon["x"+str(x)] + 15 * f, Zielcon["y"+str(x)] + 15 * f, breite / 2, hohe / 2))
            true = False
    if drucken !=0:
        if true == True: neulvl = 1


    settings1 = pygame.transform.smoothscale(settings, (30*f,30*f))
    pygame.Surface.set_alpha(settings1, alphasettings)
    screen.blit(settings1,(u(9)+23*f,r(0)+7*f))


    linien()
    außenlinien()

    #text
    font = pygame.font.Font(resource_path('ROGFonts-Regular.ttf'), int(20*f))
    fontgroß = pygame.font.Font(resource_path('ROGFonts-Regular.ttf'), int(40*f))
    #font = pygame.font.SysFont('rogfonts', int(20 * f))
    # rogfonts, arialrounded,
    #print(pygame.font.get_fonts())
    schritte = font.render("Schritte: " + str(moves), True, WHITE)
    screen.blit(schritte, (u(0)+20*f, r(0)+20*f))


    if u(9) + 21 * f < mosx < u(9) + 55 * f and r(0) + 5 * f < mosy < r(0) + 39 * f and not pygame.mouse.get_pressed()[0] == 1 and drucken != 0:
        mosoff = 1
        alphasettings = 210
    else:
        alphasettings = 180
    if (not (u(9) + 21 * f < mosx < u(9) + 55 * f and r(0) + 5 * f < mosy < r(0) + 39 * f) or drucken == 0) and mosoff == 1:
        mosoff = 0
        hold = 0


    if u(9) + 21 * f < mosx < u(9) + 55 * f and r(0) + 5 * f < mosy < r(0) + 39 * f and\
    (pygame.mouse.get_pressed()[0] == 1 and mosoff == 1 and settingswin == 0):
        alphasettings = 255
        hold = 1
    if hold == 1:
        if not pygame.mouse.get_pressed()[0] == 1:
            if hold != 3:
                hold = 2
            settingswin = 1
            soundpos = move_sound.get_volume()
            musicpos = pygame.mixer.music.get_volume()
            drucken = 2
    if settingswin == 1:
        if not alphabackground > 80:
            alphabackground += 3
            zoomf += 0.037
            if zoomf == 0.9990000000000003:
                zoomf = 1
        else:
            drucken = 3
        windowpause()
        settingspause()

    if settingswin == 0 and alphabackground > 0:
        drucken = 3
        alphabackground -= 3
        zoomf -= 0.037
        windowpause()
        settingspause()
    if settingswin == 0 and alphabackground == 0:
        drucken = 1

    if u(9) + 21 * f < mosx < u(9) + 55 * f and r(0) + 5 * f < mosy < r(0) + 39 * f and\
    (pygame.mouse.get_pressed()[0] == 1 and mosoff == 1 and settingswin == 1) or hold == 3:
        hold = 3
        alphasettings = 255
        if not pygame.mouse.get_pressed()[0] == 1:
            settingswin = 0
            mosoff = 0
            hold = 0

    if gedruckt[K_ESCAPE] and esckey == 0:
        if settingswin == 0 and drucken != 0 and neulvl == 0 and reslvl == 0:
            settingswin = 1
            soundpos = move_sound.get_volume()
            musicpos = pygame.mixer.music.get_volume()
            drucken = 2
        else:
            settingswin = 0
        esckey = 1
    if not gedruckt[K_ESCAPE] and esckey == 1:
        esckey = 0

    if gedruckt[K_r] and rkey == 0:
        if drucken != 0 and neulvl == 0 and reslvl == 0:
            reslvl = 1
            rkey = 1
    if not gedruckt[K_r] and rkey == 1:
        rkey = 0

    if start == 1:
        drucken = 0
        wait = Clock - 128
        start = 0
        neulvl = 3
        printlevel = prevlvl + 1
        alphabackground = 255
    if (reslvl == 1 or neulvl == 1 or home == 2) and stop == 1:
        if reslvl == 1:
            reslvl = 2
            settingswin = 0
        if home == 2:
            home = 3
        if neulvl == 1:
            neulvl = 2
            print("lol")
            prevlvl = currentlvl
            printlevel += 1
            settingswin = 2
        drucken = 0
        wait = Clock
        stop = 2

    außenlinien()


    if reslvl == 2:
        drucken = 0
        if wait + 61 < Clock:
            alphabackground2 -= 5
        else:
            stop = 1
            alphabackground2 += 5
        if wait + 122 == Clock:
            reslvl = 0
            drucken = 0
        settingsrect = pygame.Surface((w, h))
        settingsrect.fill(ORANGE)
        pygame.Surface.set_alpha(settingsrect, alphabackground2)
        screen.blit(settingsrect, (0, 0))
        if wait + 61 == Clock:
            if home == 3:
                home = 1
                start = -4
                settingswin = 2
                alphabackground = 255
                alphabackground2 = 0
                reslvl = 0
                drucken = 0
            stop = 0
            moves = 0


    if neulvl == 2 and wait + 45 < Clock:
        neulvl = 3
        x = y = 0
        bruh2 = pygame.draw.rect(screen, (ORANGE), (0, 0, 0, 0))
    if neulvl == 3:
        level = fontgroß.render("Level: " + str(printlevel), True, (255, 255, 255))
        screen_rect = screen.get_rect()
        text_rect = level.get_rect(center=screen_rect.center)
        print(text_rect)
        settingsrect = pygame.Surface((w,h))
        settingsrect.fill(ORANGE)
        pygame.Surface.set_alpha(settingsrect, alphabackground)
        if wait + 248 < Clock:
            alphabackground -= 5
            alphabackground2 -= 5
            sheesh()
            if alphabackground <= 0:
                alphabackground = alphabackground2 = 0
                neulvl = 0
                settingswin = 0
                drucken = 1
        else:
            if alphabackground < 255 :
                alphabackground += 2
                sheesh()
            if alphabackground >= 255 and alphabackground2 < 255:
                alphabackground2 += 5
            if wait + 248 == Clock:
                stop = 0
                currentlvl = prevlvl + 1
                moves = 0
                b = dict()
                t = dict()
                pb = dict(b)
                pt = dict(t)
        if alphabackground >= 255:
            pygame.draw.rect(screen, (ORANGE), (0, 0, w, h))
        level.set_alpha(alphabackground2)
        pygame.Surface.set_alpha(settingsrect, alphabackground)

        screen.blit(level, (text_rect))

    # print(hold, settingswin)

    pygame.display.update()
    Clock += 1
    # print(Clock)
    # (drucken)
    # print(stop)
    clock.tick(60)

