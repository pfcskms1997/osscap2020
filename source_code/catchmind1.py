#공룡게임으로 얻은 색깔 블럭 기록 받아오기
#list로 

from turtle import*
import time


#시작시간 측정
start=time.time()

pencolor("black")
title("Catch my drawing")

#화면 크기
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
    


#클릭에 따라 색칠하기
    
def drawShape(x,y):    
    pensize(30)
    a=x-x%50+25    
    b=(y//50+1)*50
    up()
    goto(a,b-15)
    down()
    goto(a,b-30)

#시작지점 50 나눈거에서 나머지빼줘야함
    
while(1):
    color=input("사용할 색을 입력하시오.(종료를 원하면 a/ 취소를 원하면 z)")
    if color =="a":
        break
 
            #elif color=="z":
        #취소에 대한 내용
    elif color=='red':
        pencolor("red")
        onscreenclick(drawShape)
        mainloop()

    elif color=='green':
        pencolor("green")
        onscreenclick(drawShape)
        mainloop()
        
    else:
            #if list[1]==0: print("green 색깔 블럭이 없습니다.")
            #else 진행
        print("잘못입력하셨습니다.")
            #LED matrix에도 위치에 따른 색 출력
        


#음성인식해서 정답일 시
        #종료시간 측정
        #종료시간 - 시작시간 보여줌
        #종료시간 - 시작시간 기록(?)

print("걸린 시간:",time.time()-start)
