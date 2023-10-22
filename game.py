import pygame
from sys import exit

pygame.init() #initializes pygame
pygame.display.set_caption('Rosalind Franklin') #sets the game name (at the tab part)
clock = pygame.time.Clock() #creates a clock object
screen = pygame.display.set_mode((800,400)) #creates game window
text_font_1 = pygame.font.Font('graphics/pixel_font.ttf', 30) #creates font we can make a title-text surface with
text_font_2 = pygame.font.Font('graphics/pixel_font.ttf', 12) #creates font we can make a description-text surface with

#creating variables for background surfaces
university_surface = pygame.image.load('graphics/university.png').convert() #creates university background surface
coal_surface = pygame.image.load('graphics/coal.png').convert() #creates coal background surface
lab_surface = pygame.image.load('graphics/lab.JPG').convert() #creates biology lab background surface

#creating variables for text surfaces and rectangles
title_surface = text_font_1.render('Rosalind\'s Double Trouble DNA Hustle', False, 'BLACK') #creates text surface for title
title_rect = title_surface.get_rect(center = (400,50))
description_surface = text_font_2.render('Help Rosalind Franklin defeat the Double Trouble Duo, '
                                         'Watson and Crick, on her journey to discover the molecular structure of DNA', False, 'BLACK') #creates text surface for game description
description_rect = description_surface.get_rect(center = (400, 80))

#creating variables for character surfaces and rectangles
crick_surface = pygame.image.load('graphics/crick.png').convert_alpha() #creates crick surface
crick_rect = crick_surface.get_rect(bottomright = (600,375)) #creates rectangle around crick with origin on the bottom right
watson_surface = pygame.image.load('graphics/watson.png').convert_alpha() #creates watson surface
watson_rect = watson_surface.get_rect(bottomright = (1500,310)) #creates rectangle around watson with origin on the bottom right corner
rosalind_surface = pygame.image.load("graphics/rosalind1.png").convert_alpha() # creates rosalind surface
rosalind_rect = rosalind_surface.get_rect(midbottom = (80,375)) #creates rectangle around rosalind with origin on the bottom middle line

#creating a variable for gravity
player_gravity = 0

while True: #runs forever (to keep the display open)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #to allow user to quit from the game
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN: #checks to see if a key was pressed
            if event.key == pygame.K_SPACE: #checks to see if the space key was pressed
                player_gravity = -20

        if event.type == pygame.KEYUP: #checks to see when the user lets go of the key
            print("up")

    #sending opening surfaces to display screen
    screen.blit(university_surface,(0,0)) #sends university background to display screen
    screen.blit(title_surface,title_rect) #sends game title to display sceen
    screen.blit(description_surface,description_rect) #sends game description to display screen

    #updates the gravity variable + rosalind
    player_gravity+=1
    rosalind_rect.y += player_gravity 
    if rosalind_rect.bottom >=375:
        rosalind_rect.bottom = 375

    #sends and moves character surfaces on display screen
    crick_rect.x -= 5 #moves crick 6 pixels to the left every loop
    watson_rect.x -= 2 #moves crick to the left every time the frame is updated
    if crick_rect.right < -100: #checks if crick walks off screen and returns him to the right of the screen
        crick_rect.left = 800
    if watson_rect.right<-100:
        watson_rect.left = 800
    screen.blit(watson_surface,watson_rect) #adds watson
    screen.blit(crick_surface,crick_rect) #sends crcik surface to display screen at the rectangle's position
    screen.blit(rosalind_surface,rosalind_rect) #sends rosalind surface to display screen at the rectangle's position




    #alternative code that could be used to see if a user presses space
    # keys = pygame.key.get_pressed
    # if keys[pygame.K_SPACE]:
    #     print('jump')
        
    #checks if characters collide
    if rosalind_rect.colliderect(crick_rect):
        print('collision')

    pygame.display.update() #updates the display
    clock.tick(60) #60 frames/second is the maximum
