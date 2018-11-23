import pygame
import random


pygame.init()

dispWidth = 800
dispHeight = 500

carWidth = 55

########################################################################
screen = pygame.display.set_mode((dispWidth,dispHeight)) #first screen to show up
menuBg = pygame.image.load('menubg.jpg')
menuBg = pygame.transform.scale(menuBg, (dispWidth, dispHeight))

insBg = pygame.image.load('insbg2.jpg') 
insBg = pygame.transform.scale(insBg, (dispWidth, dispHeight))# resize graphic

roadBg = pygame.image.load('background.png')
roadBg = pygame.transform.scale(roadBg, (dispWidth, dispHeight))# resize graphic
##########################################################################
crash_sound = pygame.mixer.Sound("crash.wav")
pygame.mixer.music.load('bgmusic.mp3')

###############################################################################
###############################################################################
carImg = pygame.image.load("diablo.png") 
carImg = pygame.transform.scale(carImg, (60, 100))# resize graphic 
carImg = carImg.convert_alpha() # remove whitespace from graphic

car2 = pygame.image.load("aventador.png") 
car2 = pygame.transform.scale(car2, (60, 100))# resize graphic
car2 = car2.convert_alpha()# remove whitespace from graphic

car3 = pygame.image.load("nsx.png")
car3 = pygame.transform.scale(car3, (60, 100)) # resize graphic
car3 = car3.convert_alpha() # remove whitespace from graphic

car4 = pygame.image.load("speeder.png")
car4 = pygame.transform.scale(car4, (60, 100)) # resize graphic
car4 = car4.convert_alpha() # remove whitespace from graphic

car5 = pygame.image.load("slr.png")
car5 = pygame.transform.scale(car5, (60, 100)) # resize graphic
car5 = car5.convert_alpha() # remove whitespace from graphic

car6 = pygame.image.load("Mach6.png")
car6 = pygame.transform.scale(car6, (60, 100)) # resize graphic
car6 = car6.convert_alpha() # remove whitespace from graphic

car7 = pygame.image.load("Stingray.png")
car7 = pygame.transform.scale(car7, (60, 100)) # resize graphic
car7 = car7.convert_alpha() # remove whitespace from graphic

car8 = pygame.image.load("bike.png")
car8 = pygame.transform.scale(car8, (60, 100)) # resize graphic
car8 = car8.convert_alpha() # remove whitespace from graphic
###############################################################################
###############################################################################

randomCars = [car2, car3, car4, car5, car6, car7, car8]
enemy = random.choice(randomCars)


clock = pygame.time.Clock()
pygame.mouse.set_visible(1)

black = (0, 0, 0)
white = (255, 255, 255)

brown = (153,102,60)
red = (200, 0, 0)
green = (0, 200, 0)

brightBrown = (240,144,47)
brightRed = (255, 0, 0)
brightGreen = (0, 255, 0)

blockColor = (53,115,255)

pause = False

#function for getting score
def score(count):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("SCORE: " + str(count), True, red)
    screen.blit(text, (0, 0))


def things(thingx, thingy, thingw, thingh, color, enemyC):
    screen.blit(enemy, [thingx, thingy, thingw, thingh])

#function for car
def car(x, y):
    screen.blit(carImg, (x, y))

#function for crashing scene
def crash():
    ####################################
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    ####################################
    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("You Crashed", largeText)
    TextRect.center = ((dispWidth / 2), (dispHeight / 2))
    screen.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Play Again", 150, 450, 100, 50, brown, brightBrown, gameLoop)
        button("Menu", 350, 450, 100, 50, brown, brightBrown, menu)
        button("Quit", 550, 450, 100, 50, brown, brightBrown, quitGame)

        pygame.display.update()
        clock.tick(15)

#function for unpause
def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False

#function for pause
def paused():
    ############
    pygame.mixer.music.pause()
    #############
    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((dispWidth / 2), (dispHeight / 2))
    screen.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Continue", 150, 450, 100, 50, brown, brightBrown, unpause)
        button("Menu", 350, 450, 100, 50, brown, brightBrown, menu)
        button("Quit", 550, 450, 100, 50, brown, brightBrown, quitGame)

        pygame.display.update()
        clock.tick(15)


#function to quit the game
def quitGame():
    pygame.quit()
    quit()

#function for text
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

#function for button
def button(msg, x, y, width, height, initialclr, afterclr, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, afterclr, (x, y, width, height))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, initialclr, (x, y, width, height))
    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (width / 2)), (y + (height / 2)))
    screen.blit(textSurf, textRect)

#function for inserting text 
def blitText(surface, text, pos, font, color=pygame.Color('yellow')):
    words = [word.split(' ') for word in text.splitlines()]
    # 2D array where each row is a list of words.
    space = font.size(' ')[0]
    # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]
                # Reset the x.
                y += word_height
                # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]
        # Reset the x.
        y += word_height
        # Start on new row.

#function for menu window    
def menu():
    menu = False
    while not menu:
        screen.fill(black)
        screen.blit(menuBg, (0,0))
        x,y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = True


        font = pygame.font.SysFont('Algerian', 70)
        text = 'Dodge Car Game'
        blitText(screen, text, (150,0), font, green)
        
        #buttons
        button("1 PLAYER", 310, 120, 230, 50, brown, brightBrown,gameLoop)
        button("2 PLAYER", 310, 185, 230, 50, brown, brightBrown)
        button("INSTRUCTIONS", 310, 248, 230, 50, brown, brightBrown,instruction)
        button("QUIT", 310, 310, 230, 50, brown, brightBrown,quitGame)
        
                
        pygame.display.flip()
        clock.tick(60)

#function for instruction window
def instruction():
    font = pygame.font.SysFont('Algerian', 22)
    txt = open('instruction.txt')
    line = txt.readline()
    text = ''
    while line:
        t = str(line)
        line = txt.readline()
        text += t

    back = False
    while not back:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                back = True


        screen.fill(white)
        screen.blit(insBg, (0,0))
        blitText(screen, text, (0,0), font)

        button("Back", 310, 450, 230, 50, brown, brightBrown,menu)
        
        pygame.display.update()


def gameLoop():
    global pause, enemy
    enemy = random.choice(randomCars)
    ############

    
    pygame.mixer.music.play(-1)
    ############
    x = (dispWidth * 0.45)
    y = (dispHeight * 0.8)

    xChange = 0

    thingStartX = random.randrange(0, dispWidth)
    thingStartY = -600
    enemySpeed = 4
    thingWidth = 55
    thingHeight = 95
    enemyC = random.choice(randomCars)
    thingCount = 1

    dodged = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xChange = -5
                if event.key == pygame.K_RIGHT:
                    xChange = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xChange = 0
        x += xChange

        screen.blit(roadBg, (0, 0))

        things(thingStartX, thingStartY, thingWidth, thingHeight, blockColor, enemyC)
        thingStartY += enemySpeed
        car(x, y)
        score(dodged)

        if x > dispWidth - carWidth or x < 0:
            crash()

        if thingStartY > dispHeight:
            thingStartY = 0 - thingHeight
            thingStartX = random.randrange(0, dispWidth)
            dodged += 1
            enemySpeed += .5


        if y < thingStartY + thingHeight:
            if x > thingStartX and x < thingStartX + thingWidth or x + carWidth > thingStartX and x + carWidth < thingStartX + thingWidth:
                crash()

        pygame.display.update()
        clock.tick(60)

        
menu()
