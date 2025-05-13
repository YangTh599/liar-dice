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

    p1 = "Thayer"
    p2 = "Lucas"
    p3 = "Apollos"
    p4 = "Josh"

    liars = liar_bar.Bar(4,p1, p2, p3 ,p4)

    p1_button = boxes.Button(window, 10, 10,200,200,p1)
    p2_button = boxes.Button(window, SCREEN_WIDTH - 210, 10,200,200,p2)
    p3_button = boxes.Button(window, 10, SCREEN_HEIGHT - 210,200,200,p3)
    p4_button = boxes.Button(window, SCREEN_WIDTH - 210, SCREEN_HEIGHT - 210,200,200,p4)

    reset = boxes.Button (window, SCREEN_WIDTH//2 -25, SCREEN_HEIGHT//2 - 25, 50,50,"RESET",BLACK)

    buttons = [p1_button, p2_button,p3_button,p4_button,reset]

    pew_safe = pygame.mixer.Sound("sounds/click.mp3")
    spy_yes = pygame.mixer.Sound("sounds/spy_yes.mp3")
    pew_bang = pygame.mixer.Sound("sounds/vine-boom.mp3")
    demo_glue = pygame.mixer.Sound("sounds/demo_glue.mp3")
    demo_idiot = pygame.mixer.Sound("sounds/demo_idiot.mp3")
    engi_ugly = pygame.mixer.Sound("sounds/engi_ugly.mp3")
    nope  = pygame.mixer.Sound("sounds/nope.mp3")
    lockednloaded = pygame.mixer.Sound("sounds/Legacy_locknload.ogg")
    enemydown = pygame.mixer.Sound("sounds/Legacy_enemydown.ogg")
    dead_ringer = pygame.mixer.Sound("sounds/dead_ringer.mp3")
    kermit = pygame.mixer.Sound("sounds/jackfilms_kermit.mp3")
    letmedie = pygame.mixer.Sound("sounds/asdf1.mp3")
    spy1 = pygame.mixer.Sound("sounds/spy1.mp3")
    spy2 = pygame.mixer.Sound("sounds/spy2.mp3")
    
    safe_sounds = [pew_safe,spy_yes,letmedie,kermit]
    revives = [lockednloaded, dead_ringer]
    deaths = [pew_bang,enemydown,spy1,spy2,demo_glue,demo_idiot,engi_ugly,nope]

    sounds = [safe_sounds, revives, deaths]

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

