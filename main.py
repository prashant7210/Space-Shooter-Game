import pygame
import random
import math
from pygame import mixer

mixer.init()
pygame.init()

# Music
mixer.music.load('bg_music.wav')
mixer.music.play(-1)

screen = pygame.display.set_mode((800, 500))  # Tuple

# Setting Icon
pygame.display.set_caption('Space Shooter :  Shoot the space Invaders')
icon = pygame.image.load('rocket.png');
pygame.display.set_icon(icon)

# Loading Background image
bg_img = pygame.image.load('space.png')

# Loading spaceship image
ship = pygame.image.load('spaceship.png')
# Spaceship position
X = 380
Y = 412
spped_x = 0

# Loading bullet image
fire = pygame.image.load('bullet.png')
flag = False
# Bullet Position
bulletX = 395
bulletY = 405

# Multiple monsters
monster_img = []
monsterX = []
monsterY = []
monster_speed_x = []
monster_speed_y = []
no_of_monsters = 6
#Loading mosnter image
for i in range(no_of_monsters):
    monster_img.append(pygame.image.load('alien.png'))
    #Intial monster position
    monsterX.append(random.randint(14, 718))
    monsterY.append(20)
    monster_speed_x.append(2)
    monster_speed_y.append(50)

# Score Font
score = 0
font = pygame.font.SysFont('Arial', 32)
def score_count():
    img = font.render(f'Score : {score}', True, 'white')
    screen.blit(img, (14, 8))

# Game Over
gv_font = pygame.font.SysFont('Arial', 64, 'bold')
def game_over():
    gv_img = gv_font.render('GAME OVER', True, 'white')
    screen.blit(gv_img, (230, 170))


running = True
while running:
    screen.blit(bg_img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # Changing X coordinate while pressing key left or right 
        if event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_LEFT):
                spped_x = -3
            if(event.key == pygame.K_RIGHT):
                spped_x = 3
            if(event.key == pygame.K_SPACE):
                flag = True
                if(bulletY == 405):
                    bullet_sound  = mixer.Sound('bull.wav')
                    bullet_sound.play()
                    bulletX = X+15
        if(event.type == pygame.KEYUP):
            spped_x = 0
    X += spped_x

    # Assure not going outside the screen
    if(X < 12):
        X = 14
    elif(X > 720):
        X = 718

    for i in range(no_of_monsters):
        # Game Over Condition
        if(monsterY[i] > 350):
            # mixer.music.pause()
            for j in range(no_of_monsters):
                monsterY[j] = 1000
            game_over()
            break

        # Monster postion
        monsterX[i] += monster_speed_x[i]
        
        # Osclliation of monster
        if(monsterX[i] < 12):
            monster_speed_x[i] = 2
            monsterY[i] += monster_speed_y[i]
        elif(monsterX[i] > 720):
            monster_speed_x[i] = -2
            monsterY[i] += monster_speed_y[i]

        # Collision between monster and bullet
        d = math.sqrt(math.pow(monsterX[i]-bulletX, 2) + math.pow(monsterY[i]-bulletY, 2))
        if(d < 35):
            bulletY = 405
            flag = False
            monsterX[i] = random.randint(14, 718)
            monsterY[i] = 20
            score+=1
            collision_sound = mixer.Sound('collide.wav')
            collision_sound.play()

        screen.blit(monster_img[i], (monsterX[i], monsterY[i]))

    # Bullet position
    if(bulletY <= 1):
        bulletY = 405
        flag = False

    if flag is True:
        screen.blit(fire, (bulletX, bulletY))
        bulletY -= 10
    screen.blit(ship, (X, Y))
    score_count()
    pygame.display.update()

print('Successfully excuted')