import pygame
import random
import math

# initializing pygame
pygame.init()

# Creating the window
window = pygame.display.set_mode((800, 600))

# Changing the title and icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# setting the background
background = pygame.image.load('rsz_backgroundresized.jpg')

# Making the Battleship
battleship = pygame.image.load('battleship.png')
battleshipx = 370
battleshipy = 480
speed_of_battleship = 0

# Making the bullet
bullet = pygame.image.load('bullet.png')
bulletx = 0
bullety = 480
bulletchangex = 0
bulletchangey = 1
bullet_state = 'ready'

# Making the Enemy Battleship
enemy_battleship = pygame.image.load('space-invaders.png')
enemy_battleshipx = random.randint(0, 736)
enemy_battleshipy = random.randint(50, 150)
enemy_changex = 0.4
enemy_changey = 40

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textx = 10
texty = 10

def score(x, y):
    score = font.render('Score :' + str(score_value), True, (255, 255, 255))
    window.blit(score, (x, y))

def baattleship(x, y):
    window.blit(battleship, (x, y))


def enemy_baattleship(x, y):
    window.blit(enemy_battleship, (x, y))


def firebullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    window.blit(bullet, (x + 16, y + 16))


def collision(enemy_battleshipx, enemy_battleshipy, bulletx, bullety):
    distance = math.sqrt((math.pow(enemy_battleshipx - bulletx, 2)) + (math.pow(enemy_battleshipy - bullety, 2)))
    if distance < 30:
        return True
    else:
        return False


# Making the window cross and minimize button work
running = True
while running:
    # Coloring the background. RGB - Red, Green, Blue
    Black = 0, 0, 0
    window.fill((0, 0, 0))
    window.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Weather any keystroke is pressed weather right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed_of_battleship = -0.5
            if event.key == pygame.K_RIGHT:
                speed_of_battleship = 0.5
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bulletx = battleshipx
                    firebullet(battleshipx, bullety)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                speed_of_battleship = 0

    # Running the battleship
    battleshipx += speed_of_battleship
    if battleshipx <= 0:
        battleshipx = 0
    elif battleshipx >= 736:
        battleshipx = 736
    baattleship(battleshipx, battleshipy)
    enemy_battleshipx += enemy_changex

    # enemy movement
    if enemy_battleshipx <= 0:
        enemy_changex = 0.4
        enemy_battleshipy += enemy_changey
    elif enemy_battleshipx >= 736:
        enemy_changex = -0.4
        enemy_battleshipy += enemy_changey
    enemy_baattleship(enemy_battleshipx, enemy_battleshipy)

    # bullet movement

    if bullety <= 0:
        bullety = 480
        bullet_state = 'ready'
    if bullet_state == 'fire':
        firebullet(bulletx, bullety)
        bullety -= bulletchangey

    # colision
    coolision = collision(enemy_battleshipx, enemy_battleshipy, bulletx, bullety)
    if coolision:
        bullety = 480
        bullet_state = 'ready'
        score_value += 1
        enemy_battleshipx = random.randint(0, 736)
        enemy_battleshipy = random.randint(50, 150)
    pygame.display.update()
    score(textx, texty)