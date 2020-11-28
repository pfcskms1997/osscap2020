import pygame
from random import *
from turtle import*
import time
import led_display as led
import threading

#################### T-REX RUN ####################
pygame.init()
Pixel = 30
win = pygame.display.set_mode((32*Pixel, 16*Pixel))

X = 3 * Pixel
Y = 16 * Pixel - Pixel
vel_x = 10
vel_y = 10
jump = False
Eaten_Box = set()
eaten_color = 0

BLACK = (0, 0, 0)
RED = (150, 0, 0)
GREEN = (0, 50, 0)
YELLOW = (255, 255, 51)
BLUE =(0, 0, 204)
PURPLE =(204, 0, 204)
SKYBLUE = (0, 216, 255)
WHITE = (255, 255, 255)
Color_Set = [RED, GREEN, YELLOW, BLUE, PURPLE, SKYBLUE, WHITE]

spd = 0.4
run = False
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
Cactus_array = [ [ 0, 0, 1, 0 ],
                 [ 0, 1, 1, 1 ], 
                 [ 0, 0, 1, 0 ], 
                 [ 0, 0, 1, 0 ] ]      

background = [[0 for x in range(32)] for x in range(16)]

def LED_init():
    t=threading.Thread(target=led.main, args=())
    t.setDaemon(True)
    t.start()
    return

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
                        led.set_pixel(int((self.x+j*Pixel)/Pixel), int((self.y+i*Pixel-5*Pixel)/Pixel), 3)
            self.Col_U_D = pygame.Rect(int(self.x+0*Pixel), int(self.y-5*Pixel), 6*Pixel, 3*Pixel)
            self.Col_L_D = pygame.Rect([int(self.x+Pixel), int(self.y-2*Pixel), 3*Pixel, 2*Pixel])
                        
        else:
            for i in range(6):
                for j in range(6):
                    if Ducked_dino_array[i][j] == 1:
                        pygame.draw.rect(win, WHITE, [int(self.x+j*Pixel), int(self.y+i*Pixel-5*Pixel), Pixel, Pixel])
                        led.set_pixel(int((self.x+j*Pixel)/Pixel), int((self.y+i*Pixel-5*Pixel)/Pixel), 3)
            self.Col_U_D = pygame.Rect(int(self.x+0*Pixel), int(self.y-3*Pixel), 6*Pixel, 2*Pixel)
            self.Col_L_D = pygame.Rect([int(self.x+1*Pixel), int(self.y-Pixel), 3*Pixel, 2*Pixel])

class Cactus():
    def __init__(self):
        self.Cacti_loc_x = 32
        self.Cacti_loc_y = 16
        self.Col_C_X = 0
        self.Col_C_Y = 0
        self.disappear = False
    def draw(self):
        if self.disappear == False:
            for i in range(4):
                for j in range(4):
                    if Cactus_array[i][j] == 1:
                        pygame.draw.rect(win, GREEN, [int((self.Cacti_loc_x*Pixel - Pixel)+j*Pixel), int((self.Cacti_loc_y * Pixel - 4*Pixel)+i*Pixel), Pixel, Pixel])
                        led.set_pixel(int(((self.Cacti_loc_x*Pixel - Pixel)+j*Pixel)/Pixel), int(((self.Cacti_loc_y*Pixel -4*Pixel)+i*Pixel)/Pixel), 3)
            self.Col_C_X = pygame.Rect(int(self.Cacti_loc_x*Pixel - 0*Pixel), int(self.Cacti_loc_y * Pixel - 3*Pixel), 3*Pixel, Pixel)
            self.Col_C_Y = pygame.Rect(int(self.Cacti_loc_x*Pixel - (-1)*Pixel), int(self.Cacti_loc_y * Pixel - 4*Pixel), Pixel, 4*Pixel)
        else:
            pass
    def update(self):
        self.Cacti_loc_x -= 1.3 * spd
        if int(self.Cacti_loc_x*Pixel - Pixel) <= 0:
            self.Cacti_loc_x = randint(32, 100)
            self.disappear = False
class Box():
    def __init__(self):   
        self.Box_loc_x = 45
        self.Box_loc_y = 16
        self.Col_B = 0
        self.rand = 7
        self.COLOR = WHITE
        self.disappear = False
    def draw(self):
        if self.disappear == False:
            pygame.draw.rect(win, self.COLOR, [int(self.Box_loc_x*Pixel - Pixel), int(self.Box_loc_y * Pixel - 10*Pixel), Pixel, Pixel])
            led.set_pixel(int((self.Box_loc_x*Pixel - Pixel)/Pixel), int((self.Box_loc_y*Pixel - 10*Pixel)/Pixel), self.rand+1)
        else:
            pass
        self.Col_B = pygame.Rect(int(self.Box_loc_x*Pixel - Pixel), int(self.Box_loc_y * Pixel - 10*Pixel), Pixel, Pixel)
    def update(self):
        self.Box_loc_x -= spd
        if int(self.Box_loc_x*Pixel - Pixel) <= 0:
            self.rand = randint(0, 6)
            self.COLOR = Color_Set[self.rand]
            self.Box_loc_x = randint(32, 100)
            self.Box_loc_y = randint(14, 20)
            self.disappear = False

class Ptera():
    def __init__(self):
        self.Ptera_loc_x = 64
        self.Ptera_loc_y = 16
        self.Col_P = 0 
        self.disappear = False

    def draw(self):
        if self.disappear == False:
            for i in range(4):
                for j in range(4):
                    if ptera_array[i][j] == 1:
                        pygame.draw.rect(win, YELLOW, [int((self.Ptera_loc_x*Pixel - Pixel)+j*Pixel), int((self.Ptera_loc_y * Pixel - 7*Pixel)+i*Pixel), Pixel, Pixel])
                        led.set_pixel(int(((self.Ptera_loc_x*Pixel - Pixel)+j*Pixel)/Pixel), int(((self.Ptera_loc_y*Pixel - 7*Pixel)+i*Pixel)/Pixel), 4)
            self.Col_P = pygame.Rect(int(self.Ptera_loc_x*Pixel - Pixel), int((self.Ptera_loc_y * Pixel - 6*Pixel)+0*Pixel), 4*Pixel, 2*Pixel)
        else:
            pass
        #pygame.draw.rect(win, ORANGE, [int(self.Ptera_loc_x*Pixel - Pixel), int(self.Ptera_loc_y * Pixel - 4*Pixel), Pixel, Pixel])
    def update(self):
        self.Ptera_loc_x -= spd * 2 
        if int(self.Ptera_loc_x*Pixel - Pixel) <= 0:
            self.Ptera_loc_x = randint(32, 100)
            self.Ptera_loc_y = randint(13, 16)
            self.disappear = False

class Fireball():
    def __init__(self):
        self.Fireball_loc_x = D.x + 6*Pixel
        self.Fireball_loc_y = 0
        self.COLOR = RED
        self.Col_F = 0
        self.collision = False
        self.Shoot = False
    def draw(self):
        pygame.draw.rect(win, self.COLOR, [self.Fireball_loc_x, self.Fireball_loc_y, Pixel, Pixel])
        led.set_pixel(int(self.Fireball_loc_x/Pixel) + 6, int((self.Fireball_loc_y)/Pixel), 1)
        self.Col_F = pygame.Rect(self.Fireball_loc_x, self.Fireball_loc_y, Pixel, Pixel)
        self.Fireball_loc_x += Pixel
    def update(self):
        if self.collision == True or self.Fireball_loc_x >= 33*Pixel:
            self.Fireball_loc_x = D.x + 6*Pixel
            self.collision = False
            self.Shoot = False
         

            # self.COLOR = choice(list(Eaten_Box)) 

class Background():
    def draw(self):
        for i in range(16):
            for j in range(32):
                if background[i][j] == 0:
                    led.set_pixel(j, i, 0)

LED_init()

S = Background()
D = Dino(X, Y)            
C = Cactus()
B = Box()
P = Ptera()
F = Fireball()
intro = True
while intro:
    win.fill(BLACK)
    D.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            intro = False
            run = False

    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_SPACE]:
        intro = False
        run = True
    pygame.display.update() 
while run:
    win.fill(BLACK)
    for i, v in enumerate(list(Eaten_Box)):
        pygame.draw.rect(win, v, [31*Pixel-i*Pixel, 0*Pixel, Pixel, Pixel])
        background[0][31-i] = 1
        for c in range(7):
            if v == Color_Set[c]:
                eaten_color = c
        led.set_pixel(int((31*Pixel - i*Pixel)/Pixel), 0, eaten_color+1)
    S.draw()
    D.draw()
    C.draw()
    B.draw()
    P.draw()
    
    # Eaten_Box.discard(F.COLOR)
    P.update()
    C.update()
    B.update()
    F.update()
    if F.Shoot:
        F.draw()
        for i in [C.Col_C_X, C.Col_C_Y]:
            if i.colliderect(F.Col_F):
                F.collision = True
                C.disappear = True
        if P.Col_P.colliderect(F.Col_F):
            P.disappear = True
            F.collision = True


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

    # Shoot
    if userInput[pygame.K_UP]:
        F.Fireball_loc_y = D.y - 3*Pixel
        # if len(Eaten_Box) != 0:
        F.Shoot = True

    # print(Eaten_Box)


    for i in [D.Col_L_D, D.Col_U_D]:
        if i.colliderect(P.Col_P):
            print("Game Over!")
            run = False
            
        if i.colliderect(B.Col_B):
            Eaten_Box.add(B.COLOR)
            B.disappear = True
        if i.colliderect(C.Col_C_X) or i.colliderect(C.Col_C_Y):
            print("Game Over!")
            run = False
            

    pygame.time.delay(25)
    pygame.display.update()
S.draw()
time.sleep(1)

#################### END of T-REX RUN ####################

mid_screen = [ [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
               [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], 
               [ 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0 ], 
               [ 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0 ], 
               [ 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0 ], 
               [ 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0 ], 
               [ 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0 ], 
               [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], 
               [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], 
               [ 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0 ], 
               [ 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1 ], 
               [ 0, 1, 0, 1, 0, 1, 0 ,0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1 ], 
               [ 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1 ], 
               [ 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0 ], 
               [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], 
               [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] ]

digit_num = [ [ [ 0, 0, 1 ], [ 0, 0, 1 ], [ 0, 0, 1 ], [ 0, 0, 1 ], [ 0, 0, 1 ] ],  #1
              [ [ 1, 1, 1 ], [ 0, 0, 1 ], [ 1, 1, 1 ], [ 1, 0, 0 ], [ 1, 1, 1 ] ],  #2
              [ [ 1, 1, 1 ], [ 0, 0, 1 ], [ 1, 1, 1 ], [ 0, 0, 1 ], [ 1, 1, 1 ] ],  #3
              [ [ 1, 0, 1 ], [ 1, 0, 1 ], [ 1, 1, 1 ], [ 0, 0, 1 ], [ 0, 0, 1 ] ],  #4
              [ [ 1, 1, 1 ], [ 1, 0, 0 ], [ 1, 1, 1 ], [ 0, 0, 1 ], [ 1, 1, 1 ] ],  #5
              [ [ 1, 1, 1 ], [ 1, 0, 0 ], [ 1, 1, 1 ], [ 1, 0, 1 ], [ 1, 1, 1 ] ],  #6
              [ [ 1, 1, 1 ], [ 1, 0, 1 ], [ 1, 0, 1 ], [ 0, 0, 1 ], [ 0, 0, 1 ] ],  #7
              [ [ 1, 1, 1 ], [ 1, 0, 1 ], [ 1, 1, 1 ], [ 1, 0, 1 ], [ 1, 1, 1 ] ],  #8
              [ [ 1, 1, 1 ], [ 1, 0, 1 ], [ 1, 1, 1 ], [ 0, 0, 1 ], [ 0, 0, 1 ] ],  #9
              [ [ 1, 1, 1 ], [ 1, 0, 1 ], [ 1, 0, 1 ], [ 1, 0, 1 ], [ 1, 1, 1 ] ] ] #0

class MidScreen():
    def draw():
       for i in range(7):
           for j in range(32):
                if mid_screen[i][j] == 1:
                    led.set_pixel(j, i, 2)
       for i in range(7, 16, 1):
           for j in range(13):
                if mid_screen[i][j] == 1:
                    led.set_pixel(j, i, 6)
           for j in range(13, 32, 1):
                if mid_screen[i][j] == 1:
                    led.set_pixel(j, i, 3)

MidScreen.draw()
time.sleep(3)
S.draw()

#################### CATCH MIND  ####################
#공룡게임으로 얻은 색깔 블럭 갯수를 colorlistcnt
#색(빨주노초파보흰) colorlist
print(Eaten_Box)
colorlist=["red", "green", "yellow", "blue", "purple", "skyblue", "white"]
colorlistcnt=[0,0,0,0,0,0,0]
for i in Eaten_Box:
    if i in Color_Set:
        colorlistcnt[Color_Set.index(i)] += 1 
        # RED, GREEN, YELLOW, BLUE, PURPLE, SKYBLUE, WHITE



print(colorlistcnt)

kkk=input("그릴 것을 입력하시오 : ")
print("그림이 완성되면 space를 누르시오")

#시작시간 측정
start=time.time()
bgcolor("black")
pencolor("white")
title("Catch my drawing")

#화면 설정
setup(1600,800)
hideturtle()
speed(0)
pensize(5)

#평행선
h=-350
for i in range(15):
    up()
    goto(-800,h)
    down()
    forward(1600)
    h+=50

#수직선
v=-750
setheading(-90)
for i in range(31):
    up()
    goto(v,-400)
    down()
    backward(800)
    v+=50
    
#색깔 별로 화면에 색칠해주기
def drawColor(color,b):
    pensize(30)
    pencolor(color)
    up()
    goto(725,b)
    down()
    goto(725,b-15)


#화면에 색깔의 존재 나타내기
for i in range(0,7,1):
    if colorlistcnt[i]>0:
        drawColor(colorlist[i],335-i*50)

#프로그램(창) 종료
def endP():
    bye()
    while(1):
        mmm=input("정답을 입력하시오 : ")
        answer(mmm)
        if (mmm==kkk):
            break
        
#정답 맞추기
def answer(mmm):
    if mmm == kkk:
        #timer = round(time.time() - start, 3)
        timer = '{:.3f}'.format(round(time.time() - start, 3)) 
        print("걸린 시간:", timer)
        ID = input("이름을 입력해주세요 : ")
        f = open("osscap2020.txt", 'a')
        data = str(timer)
        f.write(ID + ' : ' + data + 'sec' + '\n')
        f.close()
        wantList = input("기록 출력은 a, 종료는 q를 입력해주세요 : ")
        if wantList == "a":
            f = open("osscap2020.txt", 'r')
            while True:
                line = f.readline()
                if not line: break
                print(line)
            f.close()
### ending screen display ###
        else:
            f.close()

    else:print("정답이 아닙니다.")

    
#클릭에 따라 색칠하기
ledcolor = 7
def drawShape(x,y):    
    global ledcolor 
    if 700<=x<=750:
        for k in range(0,7,1):
            if 300-50*k<y<=350-50*k:
                if colorlistcnt[k]>0:  
                   pencolor(colorlist[k])
                   ledcolor = k+1
    a=x-x%50+25    
    b=(y//50+1)*50
    up()
    goto(a,b-15)
    down()
    goto(a,b-30)
    led.set_pixel(int((a+775)/50), int((400-b)/50), ledcolor)
    onkey(endP,"space")
    listen()

while 1: 
    onscreenclick(drawShape)
    mainloop()
    break


