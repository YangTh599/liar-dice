import pygame, sys
import random
import math
import os
from os.path import join
from random import randint as rnd
from pygame.time import delay as slp

from colors import *
from pygame_config import *
import classes_and_objects.shapes as shapes
import classes_and_objects.boxes as boxes

def init_game():
    """Initiates Pygame, Pygame.font, and sets the Screen window and caption"""
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption(PYGAME_CAPTION) # Window Caption
    # pygame.display.set_icon(ICON) #UNCOMMENT WHEN ICON IS DEFINED

    #Pygame Window
    window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    return window

# Draw Function to update graphics
def draw(window, buttons, dice):
    """DRAW FUNCTION | allows screen graphics to be added"""
    #BACKGROUND
    window.fill(COTTON_CANDY) # 15
    

    #FOREGROUND
    for d in dice:
        d.draw_textbox()

    for button in buttons:
        button.draw_textbox()

    #UPDATE DISPLAY
    pygame.display.update()

def handle_events(buttons,dice,sounds):
    """Handles any pygame event such as key input"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # QUIT
            return False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if buttons[0].check_clicked():
                
                for d in dice:
                    d.update_text(str(rnd(1,6)))

                sounds[0].play()
            if buttons[1].check_clicked():

                if buttons[1].text == "UNHIDE":

                    buttons[1].text = "HIDE"

                    buttons[1].rect = pygame.Rect(5, 300, 110, 20)
                elif buttons[1].text == "HIDE":

                    buttons[1].text = "UNHIDE"

                    buttons[1].rect = pygame.Rect(5, 5, 110,320)

                sounds[1].play()

                


    
    keys = pygame.key.get_pressed()

    for button in buttons:
        button.check_hover()

    return True

def main(): # MAIN FUNCTION
    """Main Function : main"""
    window = init_game()
    clock = pygame.time.Clock()
    # ADD ALL OBJECTS/CLASSES BELOW HERE

    sounds = [pygame.mixer.Sound("sounds/swoosh.mp3"),pygame.mixer.Sound("sounds/trapdoor.mp3")]

    reset = boxes.Button (window, SCREEN_WIDTH//2 -50, SCREEN_HEIGHT//2 - 25, 100,50,"REROLL",BLACK)
    hide = boxes.Button (window, 5, 5, 110,320,"UNHIDE",BLACK,PURPLE_GUY,THANOS)

    d1 = boxes.Text_box(window, 50, 10, 50, 50, str(rnd(1,6)), BLACK)
    d2 = boxes.Text_box(window, 50, 65, 50, 50, str(rnd(1,6)), BLACK)
    d3 = boxes.Text_box(window, 50, 120, 50, 50, str(rnd(1,6)), BLACK)
    d4 = boxes.Text_box(window, 50, 175, 50, 50, str(rnd(1,6)), BLACK)
    d5 = boxes.Text_box(window, 50, 235, 50, 50, str(rnd(1,6)), BLACK)

    dice = [d1,d2,d3,d4,d5]

    buttons = [reset,hide]

    # ADD ALL OBJECTS/CLASSES ABOVE HERE
    run = True
    while run: # run set to true, program runs while run is true.

        clock.tick(FPS) # FPS Tick

        run = handle_events(buttons,dice,sounds)
        

        
        draw(window, buttons,dice) # UPDATES SCREEN

    pygame.quit()
    sys.exit()
    quit()
# ADD CLASSES HERE



# ADD CLASSES ABOVE
if __name__ == "__main__": 
    main()

