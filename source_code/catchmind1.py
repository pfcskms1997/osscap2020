#아직 해결 못한거:LED 출력, 음성인식 


#공룡게임으로 얻은 색깔 블럭 갯수를 colorlistcnt
#색(빨주노초파보흰) colorlist
#colorlist=["red","orange","yellow","green","blue","purple","gray"]
colorlist=["black","red","green","yellow","blue","purple","skyblue"]
#colorlistcnt=[0,2,3,0,4,2,3]
colorlistcnt=[1,2,3,1,4,2,3]

from turtle import*
import time
import led_display as led
import threading

def LED_init():
    t=threading.Thread(target=led.main, args=())
    t.setDaemon(True)
    t.start()
    return

#시작시간 측정
start=time.time()

pencolor("black")
title("Catch my drawing")

#화면 설정
setup(1600,800)
hideturtle()
speed(100000)
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
    print("걸린 시간:",time.time()-start)
    
#클릭에 따라 색칠하기
def drawShape(x, y):    
    ledcolor = 2 
    if 700<=x<=750:
        for k in range(0,7,1):
            if 300-50*k<y<=350-50*k:
                if colorlistcnt[k]>0:
                    pencolor(colorlist[k])
                    ledcolor = k
    a=x-x%50+25    
    b=(y//50+1)*50
    up()
    goto(a,b-15)
    down()
    goto(a,b-30)
    #led.set_pixel(int((a+775)/50), int((400-b)/50), ledcolor)
    
    onkey(endP,"space")
    listen()
    
LED_init()
onscreenclick(drawShape)

### test code by MINSEONG ###
#while(1):
#pencolor("green")
#    onscreenclick(drawShape)
#    mainloop()
#############################
        
#음성인식해서 정답일 시
