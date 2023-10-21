import pygame
from sys import exit

pygame.init() #initializes pygame
pygame.display.set_caption('Rosalind Franklin') #sets the game name (at the tab part)
clock = pygame.time.Clock() #creates a clock object
screen = pygame.display.set_mode((800,400)) #creates game window
text_font_1 = pygame.font.Font('graphics/pixel_font.ttf', 30) #creates font we can make a title-text surface with
text_font_2 = pygame.font.Font('graphics/pixel_font.ttf', 12) #creates font we can make a description-text surface with

university_surface = pygame.image.load('graphics/university.png') #creates university background surface
coal_surface = pygame.image.load('graphics/coal.png') #creates coal background surface
lab_surface = pygame.image.load('graphics/lab.JPG') #creates biology lab background surface
title_surface = text_font_1.render('Rosalind\'s Double Trouble DNA Hustle', False, 'BLACK') #creates text surface for title
description_surface = text_font_2.render('Help Rosalin Franklin defeat the Double Trouble Duo '
                                         'Watson and Crick on her journey to discover the molecular structure of DNA', False, 'BLACK') #creates text surface for game description

while True: #runs forever (to keep the display open)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #to allow user to quit from the game
            pygame.quit()
            exit()

    screen.blit(university_surface,(0,0)) #sends university background to display screen
    screen.blit(title_surface,(140,50)) #sends game title to display sceen
    screen.blit(description_surface,(10, 90))

    pygame.display.update() #updates the display
    clock.tick(60) #60 frames/second is the maximum
