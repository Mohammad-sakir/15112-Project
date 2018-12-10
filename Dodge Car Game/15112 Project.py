#Name: Mohammad Saleh Ahsan Sakir
#Andrew ID: msakir

import pygame
import random

pygame.init()

dispWidth = 800
dispHeight = 500

carWidth = 55
carHeight = 95

###################################################################################
######################## BACKGROUND SECTION #######################################
###################################################################################
screen = pygame.display.set_mode((dispWidth, dispHeight)) #first screen to show up
menuBg = pygame.image.load('menubg.jpg')
menuBg = pygame.transform.scale(menuBg, (dispWidth, dispHeight))

insBg = pygame.image.load('insbg2.jpg') 
insBg = pygame.transform.scale(insBg, (dispWidth, dispHeight))# resize graphic

roadBg = pygame.image.load('background.png')
roadBg = pygame.transform.scale(roadBg, (dispWidth, dispHeight))# resize graphic
###################################################################################
######################### MUSIC SECTION ###########################################
###################################################################################
crashSound = pygame.mixer.Sound("crash.wav")
pygame.mixer.music.load('bgmusic.mp3')

###################################################################################
################### LOADING CAR IMAGES ############################################
###################################################################################
carImg1 = pygame.image.load("diablo.png") 
carImg1 = pygame.transform.scale(carImg1, (60, 100))# resize graphic 
carImg1 = carImg1.convert_alpha() # remove whitespace from graphic

carImg2 = pygame.image.load("car.png") 
carImg2 = pygame.transform.scale(carImg2, (60, 100))# resize graphic 
carImg2 = carImg2.convert_alpha() # remove whitespace from graphic

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
###################################################################################
###################################################################################
randomCars = [car2, car3, car4, car5, car6, car7]
enemy = random.choice(randomCars)

clock = pygame.time.Clock()
pygame.mouse.set_visible(1)
###################################################################################
####################### COLOR SECTION #############################################
###################################################################################
black = (0, 0, 0)
white = (255, 255, 255)
brown = (153, 102, 60)
red = (200, 0, 0)
green = (0, 200, 0)

brightBrown = (240, 144, 47)
brightRed = (255, 0, 0)
brightGreen = (0, 255, 0)
###################################################################################
###################################################################################
pause = False

#function for showing score--------------------------------------------------------
def score(count):
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render("SCORE: " + str(count), True, red)
    screen.blit(text, (0, 0))

#function for crashing scene-------------------------------------------------------
def crash(message, size, color, action):
################## Stops the music and plays the crash sound ######################
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crashSound)
###################################################################################
    largeText = pygame.font.SysFont("Algerian", size)
    TextSurf, TextRect = text_objects(message, largeText, color)
    TextRect.center = ((dispWidth / 2), (dispHeight / 2))
    screen.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
############################# BUTTONS #############################################
        button("Play Again", 150, 450, 100, 50, brown, brightBrown, action)
        button("Menu", 350, 450, 100, 50, brown, brightBrown, menu)
        button("Quit", 550, 450, 100, 50, brown, brightBrown, quitGame)
###################################################################################
        pygame.display.update()
        clock.tick(15)

#function for unpause--------------------------------------------------------------
def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False

#function for pause----------------------------------------------------------------
def paused():
###################################################################################
    pygame.mixer.music.pause()
###################################################################################
    largeText = pygame.font.SysFont("comicsansms", 115)
    TextSurf, TextRect = text_objects("Paused", largeText, black)
    TextRect.center = ((dispWidth / 2), (dispHeight / 2))
    screen.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
############################# BUTTONS #############################################
        button("Continue", 150, 450, 100, 50, brown, brightBrown, unpause)
        button("Menu", 350, 450, 100, 50, brown, brightBrown, menu)
        button("Quit", 550, 450, 100, 50, brown, brightBrown, quitGame)
###################################################################################
        pygame.display.update()
        clock.tick(15)

#function to quit the game---------------------------------------------------------
def quitGame():
    pygame.quit()
    quit()

#function for text-----------------------------------------------------------------
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

#function for button---------------------------------------------------------------
def button(msg, x, y, width, height, initialclr, afterclr, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #here whether the cursor is within the buttons boundury or not is being checked
    #if cursosr within button and pressed, it will perform the action assigned to that button
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, afterclr, (x, y, width, height))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, initialclr, (x, y, width, height))
    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText, black)
    textRect.center = ((x + (width / 2)), (y + (height / 2)))
    screen.blit(textSurf, textRect)

#function for inserting text------------------------------------------------------- 
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
        # Reset the x.
        x = pos[0]
        # Start on new row.
        y += word_height 

#function for menu window----------------------------------------------------------    
def menu():
    menu = False
    while not menu:
        screen.fill(black)
        #place the background game image
        screen.blit(menuBg, (0,0))
        x,y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = True
        #place the title
        font = pygame.font.SysFont('Algerian', 70)
        text = 'Dodge Car Game'
        blitText(screen, text, (150,0), font, green)
############################# BUTTONS #############################################
        button("1 PLAYER", 310, 120, 230, 50, brown, brightBrown,gameLoop) #button for 1 player mode
        button("2 PLAYER", 310, 185, 230, 50, brown, brightBrown,twoPlayer) #button for 2 player mode
        button("INSTRUCTIONS", 310, 248, 230, 50, brown, brightBrown,instruction) #button to know the instructions
        button("QUIT", 310, 310, 230, 50, brown, brightBrown,quitGame) #button to quit game
###################################################################################                
        pygame.display.flip()
        clock.tick(60)

#function for instruction window---------------------------------------------------
def instruction():
    #read instructions from the given file
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
        #place the given image in background
        screen.blit(insBg, (0,0))
        #place the instructions on screen from the given file
        blitText(screen, text, (0,0), font)
        #set a button for going back to main menu
        button("Back", 310, 450, 230, 50, brown, brightBrown,menu)
        
        pygame.display.update()
        
#function for one player mode------------------------------------------------------
def gameLoop():
    global pause
    enemy = random.choice(randomCars)
###################################################################################
    pygame.mixer.music.stop()
    pygame.mixer.music.play(-1)
################################################################################### 
    x = (dispWidth * 0.45)
    y = (dispHeight * 0.8)

    xChange = 0
    yChange = 0

    thingStartX = random.randrange(0, dispWidth)
    thingStartY = -600
    enemySpeed = 5
    thingWidth = 55
    thingHeight = 95
    thingCount = 1

    dodged = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #event for left and right keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xChange = -5
                if event.key == pygame.K_RIGHT:
                    xChange = 5
                
                #if 'p' is pressed, then the game will pause    
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xChange = 0
                
        #this x will change the place of the car when the associated keys will be pressed            
        x += xChange

        screen.blit(roadBg, (0, 0))

        screen.blit(enemy, [thingStartX, thingStartY, thingWidth, thingHeight])
        thingStartY += enemySpeed
        screen.blit(carImg1, (x, y))
        score(dodged)
        
        #this logic sets the border for the car
        #if the car touches the border,it will crash!
        if x > dispWidth - carWidth or x < 0:
            crash('You Crashed', 115,black, gameLoop)

        #this logic will make the enemy cars keep coming
        if thingStartY > dispHeight:
            thingStartY =0 - thingHeight
            thingStartX = random.randrange(0, dispWidth)
            dodged += 1
            enemySpeed += .5

        #this is the crash logic with the enemy
        #so if the car touches the enemy, it will crash!
        if y < thingStartY + thingHeight:
            if x > thingStartX and x < thingStartX + thingWidth or x + carWidth > thingStartX and x + carWidth < thingStartX + thingWidth:
                crash('You Crashed', 115, black, gameLoop)
            
        pygame.display.update()
        clock.tick(60)

#function for two player mode------------------------------------------------------
def twoPlayer():
    global pause
    enemy = random.choice(randomCars)
###################################################################################
    pygame.mixer.music.play(-1)
###################################################################################
    x1 = (dispWidth * 0.73)
    x2 = (dispWidth * 0.2)
    y1 = (dispHeight * 0.8)
    y2 = (dispHeight * 0.8)
    
    x1Change = 0
    x2Change = 0
    
    thingStartX = random.randrange(0, dispWidth)
    thingStartY = -600
    enemySpeed = 9
    thingWidth = 55
    thingHeight = 95

    gameExit = False
    r1 = 0
    r2 = 0
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
###################################################################################
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1Change = -5                  
                if event.key == pygame.K_RIGHT:
                    x1Change = 5
###################################################################################
                if event.key == pygame.K_a:
                    x2Change = -5
                if event.key == pygame.K_d:
                    x2Change = 5
###################################################################################
                if event.key == pygame.K_p:
                    pause = True
                    paused()
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x1Change = 0
                    r1 = 0

                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x2Change = 0
                    r2 = 0

        r1 += abs(x1Change)
        r2 += abs(x2Change)

        x1 += x1Change
        x2 += x2Change

        screen.blit(roadBg, (0, 0))

        screen.blit(enemy, [thingStartX, thingStartY, thingWidth, thingHeight])
        thingStartY += enemySpeed
        screen.blit(carImg1, (x1, y1))
        screen.blit(carImg2, (x2, y2))

        if thingStartY > dispHeight:
            thingStartY =0 - thingHeight
            thingStartX = random.randrange(0, dispWidth)
######################### LOGIC FOR PLAYER 1 ######################################
        # if p1 dodge p2, then p2 will move 
        if x1 > dispWidth - carWidth or x1 < 0 or y1 > dispHeight-carHeight or y1 < 0:
            x1Change = 0
            y1Change = 0
        #if p1 dodge enemy car, p2 will win
        if y1 < (thingStartY + thingHeight):
            if (x1 > thingStartX and x1 < thingStartX + thingWidth) or x1 + carWidth > thingStartX and x1 + carWidth < thingStartX + thingWidth:
                crash('Player 2 Won', 115, black, twoPlayer)
######################### LOGIC FOR PLAYER 2 ######################################
        #if p2 dodge p1, then p1 will move
        if x2 > dispWidth - carWidth or x2 < 0 or y2 > dispHeight-carHeight or y2 < 0:
            x2Change = 0
            y2Change = 0
        #if p2 dodge enemy car, p1 will win
        if y2 < (thingStartY + thingHeight):
            if x2 > thingStartX and x2 < thingStartX + thingWidth or x2 + carWidth > thingStartX and x2 + carWidth < thingStartX + thingWidth:
                crash('Player 1 Won', 115, red, twoPlayer)
##################### LOGIC FOR BOTH PLAYERS WHILE DODGING AT SAME TIME ###########
        #if player 1 covers more distance towards player 2, then player 2 will move
        if r1 > r2:
            if x1<x2+carWidth:
                x1Change = 0
                x2Change = -5
        #vice versa
        elif r2 > r1:
            if x2+carWidth > x1:
                x2Change = 0
                x1Change = 5
        #if the distance of both cars towards each other is same, then do nothing
        elif r1 == r2:
            if x2+carWidth>x1:
                x1Change = 0
                x2Change = 1

        pygame.display.update()
        clock.tick(60)
    
menu()
pygame.quit()
quit()


# Acknowledgement: Sentdex and stackoverflow
