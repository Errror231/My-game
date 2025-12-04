from pygame import *
from random import *
enemy_health=100
#lists
stats={
    "health": 100,
    "speed":10,
}
stats_str={
    "health":str(stats["health"]),
    "speed":str(stats["speed"]),
}

# Colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
orange= (255, 165, 0)


#x and y
#red x and y
RED_x=50
RED_y=100
#blue x and y
BLUE_y=randint(0,940)
BLUE_x=randint(0,900)

#black x and y
BLACK_y=400
BLACK_x=400
#variables
timer3=0
dmg=True
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
