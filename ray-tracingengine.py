import os
#install required packages
packages = ["pygame"]
keys = [
    "up",
    "left",
    "right",
    "down"
]
for pkg in packages:
    os.system("pip3 install {}".format(pkg))
class colors:
    white = (255, 255, 255)
    black = (0, 0, 0)
"""This module contains all of the necessary PyGame components for
running a simplified game loop.
Use it for test cases on PyGame-related code.
"""
import sys
import pygame
from pygame.locals import *
# Import additional modules here.


# Feel free to edit these constants to suit your requirements.
FRAME_RATE = 60.0
SCREEN_SIZE = (640, 480)
LINE=0
LINEtmp=0
display_surface = pygame.display.set_mode(SCREEN_SIZE)
  
# set the pygame window name
pygame.display.set_caption('pixel based rendering')
  
# create a surface object, image is drawn on it.
image = pygame.image.load(r'./rec/maps/map1.png')

def pygame_modules_have_loaded():
    success = True

    if not pygame.display.get_init:
        success = False
    if not pygame.font.get_init():
        success = False
    if not pygame.mixer.get_init():
        success = False

    return success

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.font.init()

def create_fonts(font_sizes_list):
    "Creates different fonts with one list"
    fonts = []
    for size in font_sizes_list:
        fonts.append(
            pygame.font.SysFont("Arial", size))
    return fonts
def render(screen,fnt, what, color, where):
    "Renders the fonts as passed from display_fps"
    text_to_show = fnt.render(what, 0, pygame.Color(color))
    screen.blit(text_to_show, where)
fonts = create_fonts([32, 16, 14, 8])
def display_fps(screen):
    "Data that will be rendered and blitted in _display"
    render(
        screen,
        fonts[0],
        what=str(int(clock.get_fps())),
        color="white",
        where=(0, 0))
if pygame_modules_have_loaded():
    game_screen = pygame.display.set_mode(SCREEN_SIZE)
    #pygame.display.set_caption('Test')
    clock = pygame.time.Clock()

    def declare_globals():
        # The class(es) that will be tested should be declared and initialized
        # here with the global keyword.
        # Yes, globals are evil, but for a confined test script they will make
        # everything much easier. This way, you can access the class(es) from
        # all three of the methods provided below.
        pass

    def prepare_test():
        # Add in any code that needs to be run before the game loop starts.
        pass

    def handle_input(key_name):
        global LINE
        # Add in code for input handling.
        # key_name provides the String name of the key that was pressed.
        if key_name in "up":
            LINE-=1
            print(LINE)
        elif key_name in "down":
            LINE+=1
            print(LINE)
        elif key_name in "left":
            print("Left")
        elif key_name in "right":
            print("Right")
        pass

    def update(screen, time):
        global image, LINE, LINEtmp
        if not LINE == LINEtmp:
            print("line has changed")
        display_surface.fill((70,70,70))
        for x in range(640):
            #try:
                #print(LINE)
                #display_surface.set_at((x,LINE),image.get_at((x,y-counter+LINE)))
            #except Exception as e:
                #pass
            counter=0
            
            for y in range(480):
                if image.get_at((x,y)) == (0,0,0,0):
                    counter +=1
                else:
                    try:
                        display_surface.set_at((x,y),image.get_at((x,y-counter+LINE)))
                    except Exception as e:
                        print("Error LINE most likeley overflowed/underflowed, expection attached")
                        print(e)
                    counter += 1
                #pygame.display.update()
                #import time
                #time.sleep(0.1)
        #RESET FOR UPDATE
        LINEtmp=LINE
        #display_fps(screen)
        
        #display_surface.blit(image,(0,0))
        pygame.display.update()

    # Add additional methods here.

    def main():
        declare_globals()
        prepare_test()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    key_name = pygame.key.name(event.key)
                    handle_input(key_name)

            milliseconds = clock.tick(FRAME_RATE)
            seconds = milliseconds / 1000.0
            update(game_screen, seconds)

            sleep_time = (1000.0 / FRAME_RATE) - milliseconds
            if sleep_time > 0.0:
                pygame.time.wait(int(sleep_time))
            else:
                pygame.time.wait(1)

    main()