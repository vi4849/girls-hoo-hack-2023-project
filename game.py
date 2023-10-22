import pygame
from sys import exit

pygame.init() #initializes pygame
pygame.display.set_caption('Rosalind Franklin') #sets the game name (at the tab part)
clock = pygame.time.Clock() #creates a clock object
screen = pygame.display.set_mode((800,400)) #creates game window
text_font_1 = pygame.font.Font('graphics/pixel_font.ttf', 30) #creates font we can make a title-text surface with
text_font_2 = pygame.font.Font('graphics/pixel_font.ttf', 12) #creates font we can make a description-text surface with
text_font_3 = pygame.font.Font('graphics/pixel_font.ttf', 19) #creates font we can make a description-text surface with
text_font_4 = pygame.font.Font('graphics/pixel_font.ttf', 13) #creates font we can make a description-text surface with
game_active = True #indicates that the game is active; player has not lost yet
start_game = False

#creating variables for background surfaces
university_surface = pygame.image.load('graphics/university.png').convert() #creates university background surface
coal_surface = pygame.image.load('graphics/coal.png').convert() #creates coal background surface
lab_surface = pygame.image.load('graphics/lab.JPG').convert() #creates biology lab background surface
nobel_surface = pygame.image.load('graphics/awards.jpg').convert() #creates nobel awards background surface

#creating a variable for gravity and a variable for the score
player_gravity = 0
score = 0

#creating variables for text surfaces and rectangles
title_surface = text_font_1.render('Rosalind\'s Double Trouble DNA Hustle', False, 'BLACK') #creates text surface for title
title_rect = title_surface.get_rect(center = (400,50))
description1_surface = text_font_2.render('Help Rosalind Franklin defeat the Double Trouble Duo, '
                                         'Watson and Crick, on her journey to discover the molecular structure of DNA', False, 'BLACK') #creates text surface for game description
description1_rect = description1_surface.get_rect(center = (400, 80))
description2_surface = text_font_2.render('Evade Watson and Crick so that they can\'t steal your work!', False, 'BLACK')
description2_rect = description2_surface.get_rect(center = (400, 100))
score_surface = text_font_4.render('Score: ' + f'{score}', False, 'BLACK')
score_rect = score_surface.get_rect(center = (400, 100))
rules_surface = text_font_4.render('Press \'Space\' to Start', False, 'BLACK')
rules_rect = score_surface.get_rect(center = (360, 120))
level_1_surface = text_font_1.render('Level 1: Help Rosalind Graduate College!', False, "BLACK")
level_1_rect = level_1_surface.get_rect(center = (400, 50))
lev1_desc_surface = text_font_3.render('You must evade Watson and Crick 10 times to graduate', False, "BLACK")
lev1_desc_rect = lev1_desc_surface.get_rect(center = (400, 80))
level_2_surface = text_font_1.render('Level 2: Help Rosalind Publish Coal Research!', False, "WHITE")
level_2_rect = level_1_surface.get_rect(center = (360, 50))
lev2_desc_surface = text_font_3.render('You now must evade Watson and Crick 20 times to publish', False, "WHITE")
lev2_desc_rect = lev2_desc_surface.get_rect(center = (400,80))
level_3_surface = text_font_1.render('Level 3: Help Rosalind Publish Double Helix Discovery!', False, "BLACK")
level_3_rect = level_1_surface.get_rect(center = (290, 50))
lev3_desc_surface = text_font_3.render('You now must evade Watson and Crick 30 times to win the Nobel Prize', False, "BLACK")
lev3_desc_rect = lev3_desc_surface.get_rect(center = (400, 80))
congrats1_surface = text_font_1.render('Congrats!', False, "WHITE")
congrats1_rect = congrats1_surface.get_rect(center = (400, 60))
congrats2_surface = text_font_3.render('You won the Nobel Prize!', False, "WHITE")
congrats2_rect = congrats2_surface.get_rect(center = (400, 90))

#creating variables for character surfaces and rectangles
crick_surface = pygame.image.load('graphics/crick.png').convert_alpha() #creates crick surface
crick_rect = crick_surface.get_rect(bottomright = (600,379)) #creates rectangle around crick with origin on the bottom right
watson_surface = pygame.image.load('graphics/watson.png').convert_alpha() #creates watson surface
watson_rect = watson_surface.get_rect(bottomright = (1000,280)) #creates rectangle around watson with origin on the bottom right corner
rosalind_surface = pygame.image.load("graphics/rosalind1.png").convert_alpha() # creates rosalind surface
rosalind_rect = rosalind_surface.get_rect(midbottom = (80,375)) #creates rectangle around rosalind with origin on the bottom middle line
man_surface = pygame.image.load('graphics/awardman.png').convert_alpha() #creates award man surface

while True: #runs forever (to keep the display open)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #to allow user to quit from the game
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN: #checks to see if a key was pressed
                if event.key == pygame.K_SPACE: #checks to see if the space key was pressed
                    player_gravity = -15

        else: #restarts game if player clicks space key after rosalind and W/C collision
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                crick_rect.x = 800
                watson_rect.x = 750
                score = 0

    if start_game == False:
        screen.blit(university_surface, (0, 0))  # sends university background to display screen
        screen.blit(title_surface, title_rect)  # sends game title to display screen
        screen.blit(description1_surface, description1_rect)  # sends game description to display screen
        screen.blit(description2_surface, description2_rect)
        screen.blit(rules_surface, rules_rect) # send rules surface to opening screen
        screen.blit(rosalind_surface, (385,290))  # sends rosalind surface to display screen at the rectangle's position
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            start_game = True

    if game_active and start_game: #creates the game stage in which it is active; player has not lost yet
        #sending opening surfaces to display screen
        if score < 10:
            screen.blit(university_surface, (0, 0))  # sends university background to display screen
            screen.blit(level_1_surface, level_1_rect) #sends level 1 title to display screen
            screen.blit(lev1_desc_surface,lev1_desc_rect) #sends level 1 description to display screen
            score_surface = text_font_4.render('Score: ' + f'{score}', False, 'BLACK')
            screen.blit(score_surface, score_rect)
            crick_rect.x -= 4  # moves crick 3 pixels to the left every loop
            watson_rect.x -= 2 #moves watson 1 pixel to the left every loop
            screen.blit(watson_surface, watson_rect)
            screen.blit(crick_surface, crick_rect)  # sends crick surface to display screen at the rectangle's position
            screen.blit(rosalind_surface, rosalind_rect)  # sends rosalind surface to display screen at the rectangle's position
        elif score < 20:
            screen.blit(coal_surface, (0,0)) #sends coal background to display screen
            screen.blit(level_2_surface, level_2_rect) #sends level 2 description to display
            screen.blit(lev2_desc_surface,lev2_desc_rect) #sends level 2 description to display screen
            score_surface = text_font_4.render('Score: ' + f'{score}', False, 'WHITE')
            screen.blit(score_surface, score_rect)
            crick_rect.x -= 6  # moves crick 4 pixels to the left every loop
            watson_rect.x -= 3 # moves watson 2 pixels to the left every loop
            screen.blit(watson_surface, watson_rect)
            screen.blit(crick_surface, crick_rect)  # sends crick surface to display screen at the rectangle's position
            screen.blit(rosalind_surface, rosalind_rect)  # sends rosalind surface to display screen at the rectangle's position
        elif score < 30:
            screen.blit(lab_surface, (0,0)) #sends coal background to display screen
            screen.blit(level_3_surface, level_3_rect) #sends level 2 description to display
            screen.blit(lev3_desc_surface,lev3_desc_rect) #sends level 3 description to display screen
            score_surface = text_font_4.render('Score: ' + f'{score}', False, 'BLACK')
            screen.blit(score_surface, score_rect)
            crick_rect.x -= 7 #moves crick 6 pixels to the left every loop
            watson_rect.x -= 5 # moves watson 3 pixels to the left every loop
            screen.blit(watson_surface, watson_rect)
            screen.blit(crick_surface, crick_rect)  # sends crick surface to display screen at the rectangle's position
            screen.blit(rosalind_surface, rosalind_rect)  # sends rosalind surface to display screen at the rectangle's position
        else:
            screen.blit(nobel_surface, (0,0)) #sends nobel awards background to display screen
            screen.blit(rosalind_surface, (415,220))  # sends rosalind surface to display screen on the podium
            screen.blit(man_surface, (345,210)) #sends award man surface to display screen on podium
            screen.blit(congrats1_surface, congrats1_rect) # sends congrats surface to display screen
            screen.blit(congrats2_surface, congrats2_rect)

        #updates the gravity variable + rosalind
        player_gravity+=.5
        rosalind_rect.y += player_gravity
        if rosalind_rect.bottom >=375:
            rosalind_rect.bottom = 375

        #sends and moves character surfaces on display screen
        if crick_rect.right < 0: #checks if watson walks off screen and returns him to the right of the screen
            crick_rect.left = 800
            score += 1
        if watson_rect.right < 0: #checks if watson walks off screen and returns him to the right of the screen
            watson_rect.left = 800
            score += 1

        #alternative code that could be used to see if a user presses space
        # keys = pygame.key.get_pressed
        # if keys[pygame.K_SPACE]:
        #     print('jump')

        #checks if characters collide
        if rosalind_rect.colliderect(crick_rect) or rosalind_rect.colliderect(watson_rect):
            game_active = False #ends active game stage

        

    # trivia screen
    #else: #runs if rosalind had collided with watson or crick
        #screen.fill('Red')


    pygame.display.update() #updates the display
    clock.tick(60) #60 frames/second is the maximum
