import pygame, sys, time, random, os
from pygame.locals import *
from DrawText import *
from terminate import *
from waitForPlayerToPressKey import *

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Tiptron's Space Dodger - Start Up")
WINDOWSIZE = (720, 480)
icon = pygame.transform.scale(pygame.image.load('player.png'), (32, 32))
pygame.display.set_icon(icon)
song3 = "Super Paper Mario OST - Tokens, Please.mp3"
logo = pygame.transform.scale(pygame.image.load('tiptron space dodger.png'), WINDOWSIZE)
logoR = logo.get_rect()

pygame.mixer.music.load(song3)
pygame.mixer.music.play(-1)

windowSurface = pygame.display.set_mode(WINDOWSIZE)
pygame.mouse.set_visible(False)
mainClock = pygame.time.Clock()

while True:
    windowSurface.blit(logo, logoR)
    DrawText("Normal Mode Press 1", "Pixel Emulator.otf", 32, (255, 255, 255), windowSurface, 50, 100, 350, 400)
    DrawText("Hard Mode Press 2", "Pixel Emulator.otf", 32, (255, 255, 255), windowSurface, 400, 100, 700, 400)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == ord("1"):
                os.startfile("Mini Game 1.pyw")
                pygame.quit()
                sys.exit()
            if event.key == ord("2"):
                os.startfile("Mini Game 2.pyw")
                pygame.quit()
                sys.exit()
