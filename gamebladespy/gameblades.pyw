import pygame, sys, time, os
from pygame.locals import *

WINDOWSIZE = (1, 1)
pygame.init()
pygame.mixer.init()

windowSurface = pygame.display.set_mode(WINDOWSIZE)

main_list = pygame.sprite.Group()
Images=[]
for object in sorted(os.listdir("gamebladespy"), key=len):
    if object.endswith(".png"):
        Images.append(pygame.image.load("gamebladespy//" + object))
pygame.mixer.music.load("gamebladespy//Game Blades.wav")

class window(pygame.sprite.Sprite):
    def __init__(self, imageType, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = imageType
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

def mainloop():
    windowSurface.fill((0, 0, 0))
    main_list.draw(windowSurface)
    pygame.display.update()

def gamebladeslogo(x, y, sound):
    game = window(Images[0], x, y)
    main_list.add(game)
    if sound == True:
        pygame.mixer.music.play()
    mainloop()
    time.sleep(0.4)
    game.image = Images[1]
    mainloop()
    time.sleep(0.4)
    game.image = Images[2]
    mainloop()
    time.sleep(0.4)
    game.image = Images[3]
    mainloop()
    time.sleep(0.8)
    windowSurface.fill((255, 255, 255))
    pygame.display.update()
    time.sleep(0.4)
    game.image = Images[4]
    mainloop()
    time.sleep(2)
