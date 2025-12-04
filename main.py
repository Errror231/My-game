from asyncio import timeout

import pygame

import sys
import time
from random import *

#lists
stats={
    "health": 100,
    "speed":10,
}
stats_str={
    "health":str(stats["health"]),
    "speed":str(stats["speed"]),
}
enemy_health=100
# Colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
orange= (255, 165, 0)
stage=1
# Create window
pygame.display.set_caption("The battle of shapes")
screen = pygame.display.set_mode((1000, 1000))
#x and y
#red x and y
RED_x=50
RED_y=100
#blue x and y
BLUE_y=randint(0,940)
BLUE_x=randint(0,900)
go=False
#black x and y
BLACK_y=400
BLACK_x=400
#variables
timer3=0
dmg=True
no=False
potions=True
timer=0
collide=True
collide2=True
timer_go=False
timer2=0
left=False
right=False
up=False
timer3=20
start=False
down=False
timer4=100
Damage_x=randint(0,940)
Damage_y=randint(0,900)
#def funcitons
def run2():
    global Damage_x
    global Damage_y
    global BLACK_x
    global BLACK_y
    if 400 > Damage_x:
        Damage_x += 17
    if 400 == Damage_x:
        pass
    if 400 < Damage_x:
        Damage_x -= 17
    if 400 > Damage_y:
        Damage_y += 17
    if 400 == Damage_y:
        pass
    if 400 < Damage_y:
        Damage_y -= 17
#set up the while loop for the game
while True:
    time.sleep(0.1)
    print(start)


    if start:
        Exp = pygame.image.load("Explosion.png")
        screen.blit(Exp, (RED_x, RED_y))
        if timer3 <= 0:
            start=False
            timer3=20
        else:
            timer3+=1
    #creates the timer for the games fps

    #sets the display for the health
    pygame.display.set_caption(f"battle for the shapes. health={stats_str["health"]}")
    #Extra if statements
    if timer4<=100 and no:
        timer4-=1
    else:
        no=False
        timer4=100
    if not collide2:
        Explode = pygame.image.load("Explosion.png")
        screen.blit(Explode, (BLACK_x, BLACK_y))
        timer2+=1
    if not timer_go:
        timer2+=1
    if potions==False:
        timer+=1
    if timer2 >= 20:
        collide2=True
        timer2=0
    if timer3 >= 30:
        collide2=True
        timer3=0
        timer_go = False
    if timer >= 10000:
        stats["speed"]=10
        potions=True
        collide=True
    #sets the event for quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Fill background
    screen.fill(BLACK)


    # Draw a filled red rectangle
    pygame.init()

    pygame.draw.rect(screen,BLACK, (400,400,200,200))
    The_dammager=pygame.image.load("The damager.png")
    The_dammager2=pygame.draw.rect(screen,BLACK, (Damage_x,Damage_y,200,200))
    screen.blit(The_dammager, (Damage_x,Damage_y))
    #draws the homing missile
    enemy = pygame.draw.rect(screen, BLACK, (BLACK_x, BLACK_y, 60, 50))
    if collide2 and enemy_health<=50:
        enemy = pygame.draw.rect(screen, BLACK, (BLACK_x, BLACK_y, 60, 50))
        if up:
            Missle_up_model = pygame.image.load("The up missle.png")
            screen.blit(Missle_up_model, (BLACK_x, BLACK_y))
        if down:
            Missle_down_model = pygame.image.load("The down missle.png")
            screen.blit(Missle_down_model, (BLACK_x, BLACK_y))
        if left:
            Missle_left_model = pygame.image.load("the left missle.png")
            screen.blit(Missle_left_model, (BLACK_x, BLACK_y))
        elif right:
            Missle_right_model = pygame.image.load("The right missle.png")
            screen.blit(Missle_right_model, (BLACK_x, BLACK_y))
    #draws the enemy
    main_enemy=pygame.draw.rect(screen,BLACK, (400,400,60,58
                                               ))
    main_enemy_model=pygame.image.load("The image.png")
    screen.blit(main_enemy_model, (400, 400))
    if dmg:
        pass

    #if statement for if potion spawns
    if potions:
        potion=pygame.draw.rect(screen, BLUE, (BLUE_x, BLUE_y,40,40))
        potion_model = pygame.image.load("potion.png")
        screen.blit(potion_model, (BLUE_x, BLUE_y))
    player=pygame.draw.rect(screen, BLACK, (RED_x, RED_y, 50, 50))
    player_model=pygame.image.load("An image.png")
    screen.blit(player_model, (RED_x, RED_y))
    #Collision detection for player/potion
    if player.colliderect(potion) and collide:
        potions=False
        timer=0
        stats["speed"]=30
        collide=False
        BLUE_y = randint(0, 940)
        BLUE_x = randint(0, 900)

    # Collision detection for player/missile
    if player.colliderect(enemy) and collide2 and enemy_health<=50:
        stats["health"]-=10
        collide2=False
        timer_go = True
        Explode = pygame.image.load("Explosion.png")
        start=True
        screen.blit(Explode, (RED_x, RED_y))
        BLACK_y = 400

        BLACK_x = 400
    #collisions for player/enemy


    if player.colliderect(main_enemy):
        if RED_x > 400:
            RED_x += 10
        if RED_x == 400:
            pass
        if RED_x < 400:
            RED_x -= 10
        if RED_y > 400:
            RED_y += 10
        if RED_y == 400:
            pass
        if RED_y < 400:
            RED_y -= 10
    #movement
    if pygame.key.get_pressed()[pygame.K_UP]:
        if  RED_y > 0:
            RED_y -= stats["speed"]

    if pygame.key.get_pressed()[pygame.K_DOWN]:
        if not RED_y >= 940:
         RED_y += stats["speed"]

    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        if not RED_x > 900:
            RED_x += stats["speed"]

    if pygame.key.get_pressed()[pygame.K_LEFT]:
        if  RED_x > 0:
            RED_x -= stats["speed"]

    #Enemy tracker
    if RED_x>BLACK_x:
        BLACK_x+=8
        left = True

        right=False
        up = False
        down = False
    if RED_x==BLACK_x:
        pass
    if RED_x<BLACK_x:
        BLACK_x-=8
        left=False
        right = True
        up = False
        down = False
    if RED_y>BLACK_y:
        BLACK_y+=8
        right = False
        down=True
    if RED_y==BLACK_y:
        pass
    if RED_y<BLACK_y:
        BLACK_y-=8
        left = False
        right = False
        up = True
        down = False
    # Update display
    stats_str = {
        "health": str(stats["health"]),
        "speed": str(stats["speed"]),

    }
    if player.colliderect(The_dammager2) or go and no==False:
        go=True
        run2()
    if The_dammager2.colliderect(main_enemy):
        enemy_health-=50
        no = True
    if enemy_health<=0:

        Explode2 = pygame.image.load("Explosion2.png")
        screen.blit(Explode2, (0, 0))
        time.sleep(3)
        pygame.display.set_caption("You WIN")
        break

    if stats["health"]<=0:

        pygame.display.set_caption("You have lost the game")

        break
    else:

        pygame.display.flip()

