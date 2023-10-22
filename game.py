import pygame
from sys import exit
import random

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

#creating a variable for gravity, score, and game over
player_gravity = 0
score = 0
game_over = False
count = 0
choice = random.randint(1,5)

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
                    choice = random.randint(1,5)

        else: #restarts game if player clicks space key after rosalind and W/C collision
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not game_over:
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
            choice = random.randint(1,5)

        #alternative code that could be used to see if a user presses space
        # keys = pygame.key.get_pressed
        # if keys[pygame.K_SPACE]:
        #     print('jump')

        #checks if characters collide
        if rosalind_rect.colliderect(crick_rect) or rosalind_rect.colliderect(watson_rect):
            game_active = False #ends active game stage

        

    # trivia screen
    if not game_active: #runs if rosalind had collided with watson or crick
        #use randomly generated choice to display one question
        if choice == 1:
            ORANGE = (235, 155, 52)
            screen.fill(ORANGE)
            question_surface = text_font_3.render('Even though the two-thirds of the STEM workforce is dominated by men, ', False, 'BLACK')
            question_surface1 = text_font_3.render('does that mean that women should stop pursuing careers in STEM?', False, 'BLACK')
            question_surface3 = text_font_3.render('Answer the question correctly to save your career', False, 'BLACK')

            question_rect = description2_surface.get_rect(topleft = (20, 20))
            screen.blit(question_surface,question_rect)
            screen.blit(question_surface1, (20,40))
            screen.blit(question_surface3, (20,60))

            answer_surface = text_font_3.render('Press 1 for Yes', False, 'BLACK') #use keys for user input
            answer_surface2 = text_font_3.render('Press 2 for No', False, 'BLACK')
            answer_rect = description2_surface.get_rect(topleft = (20, 100))
            screen.blit(answer_surface,answer_rect)
            screen.blit(answer_surface2,(20,130))

            key = pygame.key.get_pressed()
            if key[pygame.K_2]: #continue game
                game_active = True
                start_game = True
                crick_rect.x = 800
                watson_rect.x = 750
            elif key[pygame.K_1]: #restart game
                game_over = True
        
        if choice == 2:
            COLOR = (52, 235, 162)
            screen.fill(COLOR)
            question_surface = text_font_3.render('What can we do to encourage more girls to pursue STEM?', False, 'BLACK')
            question_surface3 = text_font_3.render('Answer the question correctly to save your career', False, 'BLACK')

            question_rect = description2_surface.get_rect(topleft = (20, 20))
            screen.blit(question_surface,question_rect)
            screen.blit(question_surface3, (20,60))

            answer_surface = text_font_3.render('Press 1 for be a role model for young girls to look up to ', False, 'BLACK')
            answer_surface2 = text_font_3.render('Press 2 for expose girls to STEM from a young age', False, 'BLACK')
            answer_surface3 = text_font_3.render('Press 3 for all of the above', False, 'BLACK')
            answer_surface4 = text_font_3.render('Press 4 for none of the above', False, 'BLACK')
            answer_rect = description2_surface.get_rect(topleft = (20, 100))
            screen.blit(answer_surface,answer_rect)
            screen.blit(answer_surface2,(20,130))
            screen.blit(answer_surface3,(20,160))
            screen.blit(answer_surface4,(20,190))


            key = pygame.key.get_pressed()
            if key[pygame.K_3]:
                game_active = True
                start_game = True
                crick_rect.x = 800
                watson_rect.x = 750
            elif key[pygame.K_1] or key[pygame.K_2] or key[pygame.K_4]:
                game_over = True
        
        
        if choice == 3:
            COLOR = (52, 195, 235)
            screen.fill(COLOR)
            question_surface = text_font_3.render('What is the point of female empowerment?', False, 'BLACK')
            question_surface3 = text_font_3.render('Answer the question correctly to save your career', False, 'BLACK')

            question_rect = description2_surface.get_rect(topleft = (20, 20))
            screen.blit(question_surface,question_rect)
            screen.blit(question_surface3, (20,60))

            answer_surface = text_font_3.render('Press 1 for to encourage women to pursue any career they want ', False, 'BLACK')
            answer_surface2 = text_font_3.render('Press 2 for to raise the status of women through education', False, 'BLACK')
            answer_surface3 = text_font_3.render('Press 3 for to accept and value female viewpoints', False, 'BLACK')
            answer_surface4 = text_font_3.render('Press 4 for all of the above', False, 'BLACK')
            answer_rect = description2_surface.get_rect(topleft = (20, 100))
            screen.blit(answer_surface,answer_rect)
            screen.blit(answer_surface2,(20,130))
            screen.blit(answer_surface3,(20,160))
            screen.blit(answer_surface4,(20,190))

            key = pygame.key.get_pressed()
            if key[pygame.K_4]:
                game_active = True
                start_game = True
                crick_rect.x = 800
                watson_rect.x = 750
            elif key[pygame.K_1] or key[pygame.K_2] or key[pygame.K_3]:
                game_over = True

        if choice == 4:
            COLOR = (104, 52, 235)
            screen.fill(COLOR)
            question_surface = text_font_3.render('Which occupation has the smallest gender pay gap?', False, 'BLACK')
            question_surface3 = text_font_3.render('Answer the question correctly to save your career', False, 'BLACK')

            question_rect = description2_surface.get_rect(topleft = (20, 20))
            screen.blit(question_surface,question_rect)
            screen.blit(question_surface3, (20,60))

            answer_surface = text_font_3.render('Press 1 for bartenders ', False, 'BLACK')
            answer_surface2 = text_font_3.render('Press 2 for physical therapists', False, 'BLACK')
            answer_surface3 = text_font_3.render('Press 3 for office clerks', False, 'BLACK')
            answer_surface4 = text_font_3.render('Press 4 for cashiers', False, 'BLACK')
            answer_rect = description2_surface.get_rect(topleft = (20, 100))
            screen.blit(answer_surface,answer_rect)
            screen.blit(answer_surface2,(20,130))
            screen.blit(answer_surface3,(20,160))
            screen.blit(answer_surface4,(20,190))

            key = pygame.key.get_pressed()
            if key[pygame.K_2]:
                game_active = True
                start_game = True
                crick_rect.x = 800
                watson_rect.x = 750
            elif key[pygame.K_1] or key[pygame.K_3] or key[pygame.K_4]:
                game_over = True


        
        if choice == 5:
            COLOR = (235, 52, 177)
            screen.fill(COLOR)
            question_surface = text_font_3.render('Fill in the blank: Women used to earn __ for every dollar that a man made, but now they make __ for every dollar that a man makes', False, 'BLACK')
            question_surface3 = text_font_3.render('Answer the question correctly to save your career', False, 'BLACK')

            question_rect = description2_surface.get_rect(topleft = (20, 20))
            screen.blit(question_surface,question_rect)
            screen.blit(question_surface3, (20,60))

            answer_surface = text_font_3.render('Press 1 for 60 cents and 82 cents', False, 'BLACK')
            answer_surface2 = text_font_3.render('Press 2 for 45 cents and  92 cents', False, 'BLACK')
            answer_surface3 = text_font_3.render('Press 3 for 38 cents and 85 cents', False, 'BLACK')
            answer_surface4 = text_font_3.render('Press 4 for 59 cents and 70 cents', False, 'BLACK')
            answer_rect = description2_surface.get_rect(topleft = (20, 100))
            screen.blit(answer_surface,answer_rect)
            screen.blit(answer_surface2,(20,130))
            screen.blit(answer_surface3,(20,160))
            screen.blit(answer_surface4,(20,190))


            key = pygame.key.get_pressed()
            if key[pygame.K_1]:
                game_active = True
                start_game = True
                crick_rect.x = 800
                watson_rect.x = 750
            elif key[pygame.K_3] or key[pygame.K_2] or key[pygame.K_4]:
                game_over = True



        if game_over:
            screen.fill('Red')
            question_surface = text_font_3.render('Oh no! Watson and Crick have stolen your work.', False, 'BLACK')
            question_rect = description2_surface.get_rect(topleft = (20, 20))
            answer_surface2 = text_font_3.render('Press r to restart', False, 'BLACK')
            answer_rect = description2_surface.get_rect(topleft = (20, 80))
            screen.blit(answer_surface2,answer_rect)
            screen.blit(question_surface,question_rect)
            key = pygame.key.get_pressed()
            if key[pygame.K_r]:
                game_over = False
                game_active = True
                start_game = False
                crick_rect.x = 800
                watson_rect.x = 750
                score = 0



    pygame.display.update() #updates the display
    clock.tick(60) #60 frames/second is the maximum
