import pygame
import time
import random

pygame.init()

crash_sound = pygame.mixer.Sound("Crash.wav")
pygame.mixer.music.load("music.mp3")

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
blue = (0, 0, 255)
red = (200, 0, 0)
green = (0, 200, 0)

bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

car_width = 73

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Atamobil")
clock = pygame.time.Clock()

carImg = pygame.image.load("racecar.png")
carImg2 = pygame.image.load("racecar2.png")
bg = pygame.image.load("bg.jpg")
logo = pygame.image.load("iconum.png")
can = pygame.image.load("can.png")

pygame.display.set_icon(logo)

pause = False
death = 0

def things_dodged(count):
    font = pygame.font.SysFont("comicsansms", 40)
    text = font.render("Skor: "+str(count), True, bright_red)
    gameDisplay.blit(text,(0,0))

def things(thingx, thingy):
    gameDisplay.blit(carImg2,(thingx,thingy))

def can_alma(can_x, can_y):
    gameDisplay.blit(can,(can_x,can_y))

def text_objects(text, font, color):
    TextSurface = font.render(text, True, color)
    return TextSurface, TextSurface.get_rect()

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def message_display(text):
    largeText = pygame.font.SysFont('monospace',115)
    TextSurf, TextRect = text_objects(text, largeText, blue)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def crash():
    global death

    death += 1

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)

    if death == 3:
        game_over()
    else:
        message_display("Çarptın!")

def Button(msg, x, y, w, h, ic, ac, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x+w > mouse[0] >x and y+h > mouse[1] >y:
            pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
            if click[0] == 1 and action != None:
                action()
        
        else:
            pygame.draw.rect(gameDisplay,ic,(x,y,w,h))

        smallText = pygame.font.SysFont("monospace", 25)
        textSurf, textRect = text_objects(msg, smallText, black)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        gameDisplay.blit(textSurf, textRect)

def unpause():
    global pause
    pause = False

    pygame.mixer.music.unpause()


def paused():

    pygame.mixer.music.pause()

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.SysFont('monospace',115)
        TextSurf, TextRect = text_objects("Durduruldu", largeText,bright_red)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        
        Button("DEVAM ET",200,450,200,80, green, bright_green,unpause)

        Button("ÇIKIŞ",550,450,200,80, red, bright_red,quit)

        pygame.display.update()
        clock.tick(15)


def game_intro():
    
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.SysFont('monospace',115)
        TextSurf, TextRect = text_objects("Atamobil", largeText,bright_red)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        
        Button("OYNA!",150,450,200,80, green, bright_green,game_loop)

        Button("ÇIKIŞ!",550,450,200,80, red, bright_red,quit)

        pygame.display.update()
        clock.tick(15)

def game_over():
    global death

    death = 0
    while death == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.SysFont('monospace',70)
        TextSurf, TextRect = text_objects("Hakkını kaybettin", largeText,bright_red)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        Button("YENİDEN OYNA!",150,450,200,80, green, bright_green,game_loop)

        Button("ÇIKIŞ!",550,450,200,80, red, bright_red,quit)

        pygame.display.update()
        clock.tick(15)

def game_loop():
    global pause

    pygame.mixer.music.play(-1)

    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(137, display_width -210)
    thing_starty = -300
    thing_speed = 3

    can_x = random.randrange(137, display_width -210)
    can_y = -300
    can_hiz = 3

    dodged = 0

    gameExit = False

    while not gameExit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        
        gameDisplay.blit(bg,(0, 0))
        things(thing_startx, thing_starty)
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)

        if dodged == 2:
            alindi = False

            while not alindi:
                can_y += can_hiz
                can_alma(can_x, can_y)

        
        if x < 137 or x > display_width-137 - car_width:
            crash()

        if thing_starty > display_height:
            thing_starty = -101
            thing_startx = random.randrange(137, display_width-137)
            dodged += 1
            thing_speed +=0.4

        if y <= thing_starty+95:
            if thing_starty < y+83:
                if x > thing_startx and x < thing_startx + 73 or x + car_width/2 > thing_startx and x + car_width/2 < thing_startx + 73 or x + car_width > thing_startx and x + car_width < thing_startx+ 73:
                    crash()

        pygame.display.update()
        clock.tick(60)
game_intro()
game_loop()
pygame.quit()
quit()