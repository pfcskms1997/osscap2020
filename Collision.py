import pygame
from random import *

pygame.init()
Pixel = 30
win = pygame.display.set_mode((32*Pixel, 16*Pixel))

X = 3 * Pixel
Y = 16 * Pixel - Pixel
vel_x = 10
vel_y = 10
jump = False
Eaten_Box = set()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (252, 168, 79)
RED = (150, 0, 0)
GREEN = (0, 50, 0)
BLUE =(0, 0, 204)
YELLOW = (255, 255, 51)
PUPPLE = (204, 0, 204)
Color_Set = [BLACK, WHITE, ORANGE, RED, GREEN, BLUE, YELLOW, PUPPLE]

speed = 0.4
run = True
dino_array = [ [ 1, 0, 0, 0, 1, 0 ],
                [ 1, 0, 0, 1, 1, 1 ], 
                [ 1, 1, 1, 1, 1, 1 ], 
                [ 1, 1, 1, 1, 0, 0 ],
                [ 0, 1, 1, 1, 0, 0 ],
                [ 0, 1, 0, 0, 0, 0 ] ]
Ducked_dino_array= [ [ 0, 0, 0, 0, 0, 0 ],
                [ 0, 0, 0, 0, 0, 0 ], 
                [ 1, 1, 1, 1, 1, 1 ], 
                [ 0, 1, 1, 1, 1, 1 ],
                [ 0, 1, 1, 1, 0, 0 ],
                [ 0, 1, 0, 0, 0, 0 ] ]
ptera_array =  [ [ 0, 0, 0, 0 ],
                   [ 0, 1, 0, 0 ], 
                   [ 1, 1, 1, 1 ], 
                   [ 0, 0, 0, 0 ] ]        

class Dino():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel_x = 10
        self.vel_y = 10
        self.Bowdown = 0
        self.Col_U_D = 0
        self.Col_L_D = 0

    def draw(self):
        if self.Bowdown == 0:
            for i in range(6):
                for j in range(6):
                    if dino_array[i][j] == 1:
                        pygame.draw.rect(win, WHITE, [int(self.x+j*Pixel), int(self.y+i*Pixel-5*Pixel), Pixel, Pixel])
            self.Col_U_D = pygame.Rect(int(self.x+0*Pixel), int(self.y-5*Pixel), 6*Pixel, 3*Pixel)
            self.Col_L_D = pygame.Rect(int(self.x+0*Pixel), int(self.y-2*Pixel), 4*Pixel, 2*Pixel)
                        
        else:
            for i in range(6):
                for j in range(6):
                    if Ducked_dino_array[i][j] == 1:
                        pygame.draw.rect(win, WHITE, [int(self.x+j*Pixel), int(self.y+i*Pixel-5*Pixel), Pixel, Pixel])
            self.Col_U_D = pygame.Rect(int(self.x+0*Pixel), int(self.y-3*Pixel), 6*Pixel, 2*Pixel)
            self.Col_L_D = pygame.Rect(int(self.x+0*Pixel), int(self.y-Pixel), 4*Pixel, 2*Pixel)

class Cactus():
    def __init__(self):
        self.Cacti_loc_x = 32
        self.Cacti_loc_y = 16
    def draw(self):
        pygame.draw.rect(win, GREEN, [int(self.Cacti_loc_x*Pixel - Pixel), int(self.Cacti_loc_y * Pixel - 2*Pixel), Pixel, Pixel])
        pygame.draw.rect(win, GREEN, [int(self.Cacti_loc_x*Pixel - Pixel), int(self.Cacti_loc_y * Pixel - 1*Pixel), Pixel, Pixel])
    def update(self):
        self.Cacti_loc_x -= speed
        if int(self.Cacti_loc_x*Pixel - Pixel) <= 0:
            self.Cacti_loc_x = randint(32, 100)
class Box():
    def __init__(self):
        self.Box_loc_x = 45
        self.Box_loc_y = 16
        self.Col_B = 0
        self.COLOR = RED
    def draw(self):
        pygame.draw.rect(win, self.COLOR, [int(self.Box_loc_x*Pixel - Pixel), int(self.Box_loc_y * Pixel - 10*Pixel), Pixel, Pixel])
        self.Col_B = pygame.Rect(int(self.Box_loc_x*Pixel - Pixel), int(self.Box_loc_y * Pixel - 10*Pixel), Pixel, Pixel)
    def update(self):
        self.Box_loc_x -= speed
        if int(self.Box_loc_x*Pixel - Pixel) <= 0:
            self.COLOR = choice(Color_Set)
            self.Box_loc_x = randint(32, 100)

class Ptera():
    def __init__(self):
        self.Ptera_loc_x = 64
        self.Ptera_loc_y = 16
        self.Col_P = 0 

    def draw(self):
        for i in range(4):
            for j in range(4):
                if ptera_array[i][j] == 1:
                    pygame.draw.rect(win, ORANGE, [int((self.Ptera_loc_x*Pixel - Pixel)+j*Pixel), int((self.Ptera_loc_y * Pixel - 7*Pixel)+i*Pixel), Pixel, Pixel])
        self.Col_P = pygame.Rect(int(self.Ptera_loc_x*Pixel - Pixel), int((self.Ptera_loc_y * Pixel - 6*Pixel)+0*Pixel), 4*Pixel, 2*Pixel)
        #pygame.draw.rect(win, ORANGE, [int(self.Ptera_loc_x*Pixel - Pixel), int(self.Ptera_loc_y * Pixel - 4*Pixel), Pixel, Pixel])
    def update(self):
        self.Ptera_loc_x -= speed * 1.5
        if int(self.Ptera_loc_x*Pixel - Pixel) <= 0:
            self.Ptera_loc_x = randint(32, 100)


D = Dino(X, Y)            
C = Cactus()
B = Box()
P = Ptera()

while run:
    win.fill(BLACK)
    D.draw()
    C.draw()
    B.draw()
    P.draw()
    P.update()
    C.update()
    B.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    userInput = pygame.key.get_pressed()
    # Ducking
    if userInput[pygame.K_DOWN]:
        D.Bowdown = Pixel
    else:
        D.Bowdown = 0
    # Jump
    if jump is False and userInput[pygame.K_SPACE]:
        jump = True
    if jump is True:
        D.y -= vel_y*4
        vel_y -= 1
        if vel_y < -10:
            jump = False
            vel_y = 10

    for i in [D.Col_L_D, D.Col_U_D]:
        if i.colliderect(P.Col_P):
            print("Game Over!")
            break
        if i.colliderect(B.Col_B):
            Eaten_Box.add(B.COLOR)



              
    


    pygame.time.delay(30)
    pygame.display.update()