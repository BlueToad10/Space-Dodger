import pygame, sys
from pygame.locals import *

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                
                if event.key == K_RETURN:
                    return
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
