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
import liar_bar

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
def draw(window, buttons):
    """DRAW FUNCTION | allows screen graphics to be added"""
    #BACKGROUND
    window.fill(WHITE) # 15
    

    #FOREGROUND
    for button in buttons:
        button.draw_textbox()

    #UPDATE DISPLAY
    pygame.display.update()

def handle_events(liars, buttons, sounds):
    """Handles any pygame event such as key input"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # QUIT
            return False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if buttons[0].check_clicked():
                liars.p1_pew.pull_trigger()

                if liars.p1_pew.status == False:
                    buttons[0].change_not_hover_color(COMMUNIST_RED)
                    buttons[0].change_hover_color(REPUBLICAN_RED)
                    sounds[2][0].play()
                    sounds[2][rnd(1,len(sounds[2]) - 1)].play()
                else:
                    sounds[0][0].play()
                    sounds[0][rnd(1,len(sounds[0]) - 1)].play()
            if buttons[1].check_clicked():
                liars.p2_pew.pull_trigger()

                if liars.p2_pew.status == False:
                    buttons[1].change_not_hover_color(COMMUNIST_RED)
                    buttons[1].change_hover_color(REPUBLICAN_RED)
                    sounds[2][0].play()
                    sounds[2][rnd(1,len(sounds[2]) - 1)].play()
                else:
                    sounds[0][0].play()
                    sounds[0][rnd(1,len(sounds[0]) - 1)].play()
            if buttons[2].check_clicked():
                liars.p3_pew.pull_trigger()

                if liars.p3_pew.status == False:
                    buttons[2].change_not_hover_color(COMMUNIST_RED)
                    buttons[2].change_hover_color(REPUBLICAN_RED)
                    sounds[2][0].play()
                    sounds[2][rnd(1,len(sounds[2]) - 1)].play()
                else:
                    sounds[0][0].play()
                    sounds[0][rnd(1,len(sounds[0]) - 1)].play()
            if buttons[3].check_clicked():
                liars.p4_pew.pull_trigger()

                if liars.p4_pew.status == False:
                    buttons[3].change_not_hover_color(COMMUNIST_RED)
                    buttons[3].change_hover_color(REPUBLICAN_RED)
                    sounds[2][0].play()
                    sounds[2][rnd(1,len(sounds[2]) - 1)].play()
                else:
                    sounds[0][0].play()
                    sounds[0][rnd(1,len(sounds[0]) - 1)].play()

            if buttons[4].check_clicked():

                for pew in liars.pews:
                    pew.reset()
                    sounds[1][rnd(0,len(sounds[1]) - 1)].play()

                for button in buttons:
                    button.change_not_hover_color(THAYER_GREEN)
                    button.change_hover_color(LIME)

            

                


    
    keys = pygame.key.get_pressed()

    for button in buttons:
        button.check_hover()

    return True

def main(): # MAIN FUNCTION
    """Main Function : main"""
    window = init_game()
    clock = pygame.time.Clock()
    # ADD ALL OBJECTS/CLASSES BELOW HERE

    reset = boxes.Button (window, SCREEN_WIDTH//2 -25, SCREEN_HEIGHT//2 - 25, 50,50,"RESET",BLACK)

    d1 = boxes.Text_box(window, 10, 10, 50, 50, str(rnd(1,6)), BLACK)
    d2 = boxes.Text_box(window, 10, 65, 50, 50, str(rnd(1,6)), BLACK)
    d3 = boxes.Text_box(window, 10, 120, 50, 50, str(rnd(1,6)), BLACK)
    d4 = boxes.Text_box(window, 10, 175, 50, 50, str(rnd(1,6)), BLACK)
    d5 = boxes.Text_box(window, 10, 10, 50, 50, str(rnd(1,6)), BLACK)

    buttons = [reset]

    # ADD ALL OBJECTS/CLASSES ABOVE HERE
    run = True
    while run: # run set to true, program runs while run is true.

        clock.tick(FPS) # FPS Tick

        run = handle_events(liars, buttons,sounds)
        

        
        draw(window, buttons) # UPDATES SCREEN

    pygame.quit()
    sys.exit()
    quit()
# ADD CLASSES HERE



# ADD CLASSES ABOVE
if __name__ == "__main__": 
    main()

