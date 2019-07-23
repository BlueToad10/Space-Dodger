import pygame, random, sys, time
from pygame import *
from DrawText import *
from terminate import *
from waitForPlayerToPressKey import *

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Tiptron's Space Dodger - Hard Mode")
WINDOWSIZE = (720, 480)
FPS = 60
BADDIEMINSPEED = 1
BADDIEMAXSPEED = 8
ADDNEWBADDIERATE = 6
BACKGROUNDCOLOUR = (0, 0, 0)
moveLeft=moveRight=False
playerHealth = 30
cooldown=120
playerPosX=points=spawnCounter=pointCounter=countUpPoints = 0
icon = pygame.transform.scale(pygame.image.load('player.png'), (32, 32))
pygame.display.set_icon(icon)
playerImage = pygame.transform.scale(pygame.image.load('player.png'), (64, 64))
backgroundImage = pygame.transform.scale(pygame.image.load('background.png'), WINDOWSIZE)
logo = pygame.transform.scale(pygame.image.load('tiptron space dodger.png'), WINDOWSIZE)
healthBar = pygame.image.load('healthBar.png')
pointBar = pygame.image.load('pointBar.png')
song1 = "Super Paper Mario OST - Pit of 100 Trials.mp3"
song2 = "Super Paper Mario OST - Minigame Over.mp3"
song3 = "Super Paper Mario OST - Tokens, Please.mp3"
sound1 = pygame.mixer.Sound("SE1_P_MARIO_DAMAGE1.wav")
sound2 = pygame.mixer.Sound("SE4_I_POWERPLUS1.wav")
sound3 = pygame.mixer.Sound("SE4_I_RECOVER_HP_BIG1.wav")
enemyImages=[]
itemImages=[]
for i in range(13):
    enemyImages.append(pygame.transform.scale(pygame.image.load('enemy_' + str(i + 1) + '.png'), (64, 64)))
for i in range(19):
    itemImages.append(pygame.transform.scale(pygame.image.load('item_' + str(i + 1) + '.png'), (64, 64)))
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
        pygame.sprite.Sprite.__init__(self)
        self.baddie = random.randint(0,1)
        self.image = playerImage
        if self.baddie == 1:
            self.image = enemyImages[random.randint(0,12)]
        elif self.baddie == 0:
            self.image = itemImages[random.randint(0,18)]
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,500)
        self.rect.y = -64
        self.speed = random.randint(2, 8)
    def update(self):
        global spawnrate, points, playerHealth, cooldown, pointCounter
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
                playerHealth += 10
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

player_list=pygame.sprite.Group()
background_list=pygame.sprite.Group()
objects_list=pygame.sprite.Group()
windowSurface = pygame.display.set_mode(WINDOWSIZE)
pygame.mouse.set_visible(False)
mainClock = pygame.time.Clock()

background_list.add(background(logo))
background_list.draw(windowSurface)
DrawText("Press any key", "Pixel Emulator.otf", 32, (255, 255, 255), windowSurface, 10, 10, 400, 100)
pygame.display.update()
pygame.mixer.music.load(song3)
pygame.mixer.music.play(-1)
waitForPlayerToPressKey()

background_list.add(background(backgroundImage))
background_list.add(infoBar(10, 30, pointBar))
background_list.add(infoBar(550, 10, healthBar))
while True:
    player_list.add(player(320, 400))
    pygame.mixer.music.load(song1)
    pygame.mixer.music.play(-1)
    while True:
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
        DrawText(str(countUpPoints), "Pixel Emulator.otf", 32, (255, 255, 255), windowSurface, 80, 0, 300, 100)
        DrawText(str(playerHealth), "Pixel Emulator.otf", 32, (255, 255, 255), windowSurface, 610, 0, 1080, 00)
        objects_list.draw(windowSurface)
        pygame.display.update()
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
        spawnCounter += 1
        if cooldown < 120:
            cooldown += 1
        if spawnCounter >= spawnrate:
            objects_list.add(objects())
            spawnCounter = 0
        mainClock.tick(FPS)
        if playerHealth <= 0:
            break
    pygame.mixer.music.load(song2)
    pygame.mixer.music.play(-1)
    DrawText("Game Over", "Pixel Emulator.otf", 32, (255, 255, 255), windowSurface, 300, 100, 400, 100)
    pygame.display.update()
    waitForPlayerToPressKey()
    playerHealth=30
    points=countUpPoints=0
    objects_list.empty()
    player_list.empty()
    
