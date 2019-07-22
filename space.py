import pygame, random, sys
from pygame.locals import *

WINDOWWIDTH = 600
WINDOWHEIGHT = 600
TEXTCOLOR = (255, 255, 255)
BACKGROUNDCOLOR = (0, 0, 0)
FPS = 60
BADDIEMINSIZE = 10
BADDIEMAXSIZE = 40
BADDIEMINSPEED = 1
BADDIEMAXSPEED = 8
ADDNEWBADDIERATE = 6
PLAYERMOVERATE = 5

def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                return

def playerHasHitBaddie(playerRect, baddies):
    for b in baddies:
        if playerRect.colliderect(b['rect']):
            return True
    return False

def playerHasHitFood(playerRect, food):
    for f in food:
        if playerRect.colliderect(f['rect']):
            return True
    return False

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Dodger')
pygame.mouse.set_visible(False)

font = pygame.font.SysFont(None, 48)

gameOverSound = pygame.mixer.Sound('death.ogg')
pygame.mixer.music.load('background.ogg')

background = pygame.image.load('background.png')
earth = pygame.image.load('earth.png')

earthImage = pygame.image.load('earth.png')

playerImage = pygame.image.load('player.png')
playerRect = playerImage.get_rect()
baddieImage = pygame.image.load('baddie.png')
foodImage = pygame.image.load('cherry.gif')

drawText('Dodger', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
drawText('Press a key to start.', font, windowSurface, (WINDOWWIDTH / 3) -30, (WINDOWHEIGHT / 3) + 50)
pygame.display.update()
waitForPlayerToPressKey()


timeCounter = 0
topScore = 0
while True:
    windowSurface.fill(BACKGROUNDCOLOR)
    drawText('This was once a planet of hope but', font, windowSurface, (WINDOWWIDTH / 25), (WINDOWHEIGHT / 18))
    drawText('is now just pieces of rock and dirt.', font, windowSurface, (WINDOWWIDTH / 25), (WINDOWHEIGHT / 10))
    drawText('(press button)', font, windowSurface, (WINDOWWIDTH / 25), (WINDOWHEIGHT / 3))
    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    drawText('you must see how far you can go to', font, windowSurface, (WINDOWWIDTH / 25), (WINDOWHEIGHT / 6))
    drawText('restore the world', font, windowSurface, (WINDOWWIDTH / 25), (WINDOWHEIGHT / 4))
    drawText('(press button)', font, windowSurface, (WINDOWWIDTH / 25), (WINDOWHEIGHT / 3))
    pygame.display.update()
    waitForPlayerToPressKey()
    windowSurface.fill(BACKGROUNDCOLOR)
    drawText('use keys (up down left right or', font, windowSurface, (WINDOWWIDTH / 25), (WINDOWHEIGHT / 20))
    drawText('w s a d) and x to move at light speed.', font, windowSurface, (WINDOWWIDTH / 25), (WINDOWHEIGHT / 10))
    drawText('(press button)to start the game.', font, windowSurface, (WINDOWWIDTH / 25), (WINDOWHEIGHT / 3)+ 50)
    pygame.display.update()
    waitForPlayerToPressKey()
    baddies = []
    score = 0
    timeCounter = 0
    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    pygame.display.background = (WINDOWWIDTH / 17, WINDOWHEIGHT / 17)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    baddieAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)

    pygame.display.update()

    while True:
        score += 1
        timeCounter += 1
        
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
 
            if event.type == KEYDOWN:
                if event.key == ord('x'):
                    slowCheat = True
                if event.key == K_LEFT or event.key == ord('a'):
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == ord('w'):
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == ord('s'):
                    moveUp = False
                    moveDown = True

                pygame.display.update()
                    
            if event.type == KEYUP:
                if event.key == ord('x'):
                    slowCheat = False
                if event.key == K_ESCAPE:
                        terminate()

                pygame.display.update()

                if event.key == K_LEFT or event.key == ord('a'):
                    moveLeft = False
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveRight = False
                if event.key == K_UP or event.key == ord('w'):
                    moveUp = False
                if event.key == K_DOWN or event.key == ord('s'):
                    moveDown = False

                pygame.display.update()

            if event.type == MOUSEMOTION:
                playerRect.move_ip(event.pos[0] - playerRect.centerx,event.pos[1] - playerRect.centery)

            if not reverseCheat and not slowCheat or timeCounter == 100:
               baddieAddCounter += 1
            if baddieAddCounter == ADDNEWBADDIERATE:
                baddieAddCounter = 0
                baddieSize = random.randint(BADDIEMINSIZE, BADDIEMAXSIZE)
                newBaddie = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH-baddieSize), 0 - baddieSize, baddieSize, baddieSize),
                             'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                             'surface':pygame.transform.scale(baddieImage, (baddieSize, baddieSize)),
                             }

                pygame.display.update()

                baddies.append(newBaddie)
                
                if timeCounter == 100:
                    baddies.append(newBaddie)
                    timeCounter = 0
                    timeCounter += 1

            if moveLeft and playerRect.left > 0:
                playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
                pygame.display.update()
            if moveRight and playerRect.right < WINDOWWIDTH:
                playerRect.move_ip(PLAYERMOVERATE, 0)
                pygame.display.update()
            if moveUp and playerRect.top > 0:
                playerRect.move_ip(0, -1 * PLAYERMOVERATE)
                pygame.display.update()
            if moveDown and playerRect.bottom < WINDOWHEIGHT:
                pygame.display.update()
                playerRect.move_ip(0, PLAYERMOVERATE)

            pygame.display.update()

            pygame.mouse.set_pos(playerRect.centerx, playerRect.centery)

        for b in baddies:
            if not reverseCheat and not slowCheat:
                b['rect'].move_ip(0, b['speed'])
            elif reverseCheat:
                b['rect'].move_ip(0, -5)
            elif slowCheat:
                b['rect'].move_ip(0, 1)
        
        for b in baddies[:]:
            if b['rect'].top > WINDOWHEIGHT:
                baddies.remove(b)

        pygame.display.update()
        
        windowSurface.fill(BACKGROUNDCOLOR)

        drawText('Score: %s' % (score), font, windowSurface, 10, 0)
        drawText('Top Score: %s' % (topScore), font, windowSurface, 10, 40)

        pygame.display.update()

        windowSurface.blit(playerImage, playerRect)

        for b in baddies:
            windowSurface.blit(b['surface'], b['rect'])

            pygame.display.update()
            
        if playerHasHitBaddie(playerRect, baddies):
            if score > topScore:
                topScore = score
            break

        mainClock.tick(FPS)

        pygame.display.update()

        if timeCounter == 100 or timeCounter == 111 or timeCounter == 90 or timeCounter == 55 or timeCounter == 22or timeCounter == 11 or timeCounter == 22 or timeCounter == 33 or timeCounter == 15:
            timeCounter = 0
            timeCounter += 1
            baddieAddCounter += 1
            if baddieAddCounter == ADDNEWBADDIERATE:
                baddieAddCounter = 0
                baddieSize = random.randint(BADDIEMINSIZE, BADDIEMAXSIZE)
                newBaddie = {'rect': pygame.Rect(random.randint(0, WINDOWWIDTH-baddieSize), 0 - baddieSize, baddieSize, baddieSize),
                             'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                             'surface':pygame.transform.scale(baddieImage, (baddieSize, baddieSize)),
                             }

                pygame.display.update()

                baddies.append(newBaddie)

        if topScore == 65000:
            topScore = 0

        if score == 5:
            pygame.mixer.music.load('background.ogg')
            pygame.mixer.music.play(-1, 0.0)
            baddieImage = pygame.image.load('baddie.png')

        if score == 5000:
            print('one out of seven magic crystals collected.')
            print('now entering water region.')
            pygame.mixer.music.load('water.ogg')
            pygame.mixer.music.play(-1, 0.0)
            baddieImage = pygame.image.load('water regen.png')

        if score == 10000:
            print('two out of seven magic crystals collected.')
            print('now entering grassy region.')
            pygame.mixer.music.load('grass.ogg')
            pygame.mixer.music.play(-1, 0.0)
            baddieImage = pygame.image.load('grassy regen.png')

        if score == 17500:
            print('three out of seven magic crystals collected.')
            print('now entering the stone region.')
            pygame.mixer.music.load('stone.ogg')
            pygame.mixer.music.play(-1, 0.0)
            baddieImage = pygame.image.load('stone.png')
            
        if score == 22500:
            print('four out of seven magic crystals collected.')
            print('watch out lava.')
            pygame.mixer.music.load('lava.ogg')
            pygame.mixer.music.play(-1, 0.0)
            baddieImage = pygame.image.load('lava.png')

        if score == 30000:
            print('five out of seven magic crystals collected.')
            print('be careful of near by stars.')
            pygame.mixer.music.load('stars.ogg')
            pygame.mixer.music.play(-1, 0.0)
            baddieImage = pygame.image.load('star.png')

        if score == 45000:
            print('six out of seven magic crystals collected.')
            print('oh no lots of monsters are trying to get us.')
            print('thay will be destroyed if we restore the earth.')
            pygame.mixer.music.load('monsters.ogg')
            pygame.mixer.music.play(-1, 0.0)
            baddieImage = pygame.image.load('minyon.png')

        if score == 65000:
            pygame.mixer.music.stop()
            windowSurface.fill(BACKGROUNDCOLOR)
            drawText('the seven crystals have been colected', font, windowSurface, (WINDOWWIDTH / 20), (WINDOWHEIGHT / 20))
            pygame.display.update()
            waitForPlayerToPressKey()
            windowSurface.fill(BACKGROUNDCOLOR)
            drawText('the earth has been restored', font, windowSurface, (WINDOWWIDTH / 20), (WINDOWHEIGHT / 20))
            pygame.display.update()
            waitForPlayerToPressKey()
            windowSurface.fill(BACKGROUNDCOLOR)
            drawText('!YOU WON THE GAME!', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
            drawText('Press a key to play again.', font, windowSurface, (WINDOWWIDTH / 3 - 80), (WINDOWHEIGHT / 3) + 50)
            pygame.display.update()
            waitForPlayerToPressKey()
            if score > topScore:
               topScore = score
            break
            pygame.display.update()

    pygame.mixer.music.stop()
    gameOverSound.play()

    drawText('GAME OVER', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3))
    drawText('Press a key to play again.', font, windowSurface, (WINDOWWIDTH / 3) - 80, (WINDOWHEIGHT / 3) + 50)
    pygame.display.update()
    waitForPlayerToPressKey()
    
    pygame.display.update()

    gameOverSound.stop()
