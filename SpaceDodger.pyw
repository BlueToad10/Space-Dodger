import pygame, sys, time, random, os
from pygame.locals import *
from assets.DrawText import *
from assets.terminate import *
from assets.waitForPlayerToPressKey import *
from gamebladespy.gameblades import *

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Space Dodger - Start Up")
WINDOWSIZE = (720, 480)
icon = pygame.transform.scale(pygame.image.load('assets//images//player.png'), (32, 32))
pygame.display.set_icon(icon)
song3 = "assets//music//space dodger title.mp3"
logo = pygame.transform.scale(pygame.image.load('assets//images//logo.png'), WINDOWSIZE)
logoR = logo.get_rect()
font = "assets//Pixel Emulator.otf"

Uphealth = 0
BACKGROUNDCOLOUR = (0, 0, 0)
FPS=60
moveLeft=moveRight=False
playerHealth = 100
cooldown=120
playerPosX=points=spawnCounter=pointCounter=countUpPoints = 0
playerImage = pygame.transform.scale(pygame.image.load('assets//images//player.png'), (64, 64))
backgroundImage = pygame.transform.scale(pygame.image.load('assets//images//background.png'), WINDOWSIZE)
songlist = []
song1 = "assets//music//space dodger 1.mp3"
song2 = "assets//music//space dodger 2.mp3"
songlist.append(song1)
songlist.append(song2)
sound1 = pygame.mixer.Sound("assets//sounds//hit 1.wav")
sound2 = pygame.mixer.Sound("assets//sounds//item get.wav")
sound3 = pygame.mixer.Sound("assets//sounds//health up.wav")
sound4 = pygame.mixer.Sound("assets//sounds//hit 2.wav")
enemyImages=[]
itemImages=[]
enemiesNum=itemsNum=-1
for object in os.listdir("assets//images//enemies"):
    enemyImages.append(pygame.transform.scale(pygame.image.load("assets//images//enemies//" + object), (64, 64)))
    enemiesNum+=1
for object in os.listdir("assets//images//items"):
    itemImages.append(pygame.transform.scale(pygame.image.load("assets//images//items//" + object), (64, 64)))
    itemsNum+=1
spawnrate = random.randint(6,48)

class player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = playerImage
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rectX = x
        self.rectY = y
    def update(self):
        global playerPosX
        self.rect.x = self.rectX + playerPosX
        
class objects(pygame.sprite.Sprite):
    def __init__(self):
        global enemiesNum, itemsNum
        pygame.sprite.Sprite.__init__(self)
        self.baddie = random.randint(0,1)
        self.image = playerImage
        if self.baddie == 1:
            self.image = enemyImages[random.randint(0,enemiesNum)]
        elif self.baddie == 0:
            self.image = itemImages[random.randint(0,itemsNum)]
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,500)
        self.rect.y = -64
        self.speed = random.randint(2, 8)
    def update(self):
        global spawnrate, points, playerHealth, cooldown, pointCounter, Uphealth
        self.rect.y += self.speed
        if self.baddie == 1:
            if pygame.sprite.spritecollideany(self, player_list) and cooldown >= 120:
                playerHealth -= 10
                cooldown=0
                spawnrate = random.randint(6,48)
                sound1.play()
        elif self.baddie == 0 and pygame.sprite.spritecollideany(self, player_list):
            points += 100
            pointCounter += 100
            self.remove(objects_list)
            spawnrate = random.randint(6,48)
            sound2.play()
            if pointCounter == 9000:
                playerHealth += Uphealth
                pointCounter = 0
                sound3.play()
        if self.rect.y > 480:
            self.remove(objects_list)

class background(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

class infoBar(pygame.sprite.Sprite):
    def __init__(self, x, y, bar):
        pygame.sprite.Sprite.__init__(self)
        self.image = bar
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

def music():
    if pygame.mixer.music.get_busy() == False:
        flip = random.randint(0,10)
        if flip >= 10:
            pygame.mixer.music.load(song1)
        elif flip >= 7:
            pygame.mixer.music.load(song2)
        elif flip >= 0:
            pygame.mixer.music.load(song3)
        pygame.mixer.music.play(1)

player_list=pygame.sprite.Group()
background_list=pygame.sprite.Group()
objects_list=pygame.sprite.Group()
windowSurface = pygame.display.set_mode(WINDOWSIZE)
gamebladeslogo(720/4, 480/3, True)
pygame.mouse.set_visible(False)
mainClock = pygame.time.Clock()

pygame.mixer.music.load(song3)
pygame.mixer.music.play(-1)

windowSurface = pygame.display.set_mode(WINDOWSIZE)
pygame.mouse.set_visible(False)
mainClock = pygame.time.Clock()

def MiniGame(Health, luheart):
    global playerPosX, cooldown, playerHealth, Uphealth, moveLeft, moveRight, countUpPoints, points, spawnCounter, spawnrate
    player_list.add(player(320, 400))
    flip = random.randint(0,10)
    if flip >= 10:
        pygame.mixer.music.load(song1)
    elif flip >= 7:
        pygame.mixer.music.load(song2)
    elif flip >= 0:
        pygame.mixer.music.load(song3)
    pygame.mixer.music.play(1)
    playerHealth = Health
    Uphealth = luheart
    pygame.display.set_caption("Space Dodger - Normal Mode")
    background_list.add(background(logo))
    background_list.draw(windowSurface)
    background_list.add(background(backgroundImage))
    while True:
        music()
        if moveLeft == True and moveRight == False and playerPosX > -320:
            playerPosX -= 8
        if moveRight == True and moveLeft == False and playerPosX < 336:
            playerPosX += 8
        player_list.update()
        objects_list.update()
        background_list.draw(windowSurface)
        player_list.draw(windowSurface)
        if countUpPoints < points:
            countUpPoints += 10
        DrawText("score:" + str(countUpPoints), font, 32, (255, 255, 255), windowSurface, 10, 0, 300, 100)
        DrawText("hp:" + str(playerHealth), font, 32, (255, 255, 255), windowSurface, 570, 0, 1080, 00)
        objects_list.draw(windowSurface)
        pygame.display.update()
        mainClock.tick(FPS)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == K_LEFT:
                    moveLeft = True
                if event.key == K_RIGHT:
                    moveRight = True
            if event.type == KEYUP:
                if event.key == K_LEFT:
                    moveLeft = False
                if event.key == K_RIGHT:
                    moveRight = False
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        spawnCounter += 1
        if cooldown < 120:
            cooldown += 1
        if spawnCounter >= spawnrate:
            objects_list.add(objects())
            spawnCounter = 0
        if playerHealth <= 0:
            break
    pygame.mixer.music.stop()
    sound4.play()
    time.sleep(4)
    pygame.mixer.music.load(song3)
    pygame.mixer.music.play(-1)
    DrawText("Game Over", font, 32, (255, 255, 255), windowSurface, 300, 100, 400, 100)
    pygame.display.update()
    waitForPlayerToPressKey()
    playerHealth=Health
    points=countUpPoints=0
    objects_list.empty()
    player_list.empty()
    
while True:
    windowSurface.blit(logo, logoR)
    DrawText("Normal Mode Press 1", font, 32, (255, 255, 255), windowSurface, 50, 100, 350, 400)
    DrawText("Hard Mode Press 2", font, 32, (255, 255, 255), windowSurface, 400, 100, 700, 400)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == ord("1"):
                MiniGame(100, 50)
            elif event.key == ord("2"):
                MiniGame(30, 10)
