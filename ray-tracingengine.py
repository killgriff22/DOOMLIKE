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
display_surface = pygame.display.set_mode(SCREEN_SIZE)
  
# set the pygame window name
pygame.display.set_caption('Image')
  
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

if pygame_modules_have_loaded():
    game_screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('Test')
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
        # Add in code for input handling.
        # key_name provides the String name of the key that was pressed.
        if key_name in "up":
            print("Up")
        elif key_name in "down":
            print("Down")
        elif key_name in "left":
            print("Left")
        elif key_name in "right":
            print("Right")
        pass

    def update(screen, time):
        global image
        print(pygame.image.load("./rec/maps/map1.png"))
        display_surface.fill((70,70,70))
        display_surface.blit(image,SCREEN_SIZE)
        #RESET FOR UPDATE
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