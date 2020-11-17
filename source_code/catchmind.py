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
    


#
def drawShape(x,y):    
    pensize(50)
    up()
    goto(x,y)
    down()
    goto(x,y-25)
    onscreenclick(None)    
    

#


        
#색칠하기    

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
        

#색 정하고 클릭한 칸 fill
        
        #onscreenclick:화면내의 특정지점을 클릭하면 그 좌표를 기억하고 실행하는 함수
        #화면 클릭 시 함수 실행
        # 실행되는 함수는 현재 좌표(클릭 지점)인 (x,y)를 매개변수로 이용


#음성인식해서 정답일 시
        #종료시간 측정
        #종료시간 - 시작시간 보여줌
        #종료시간 - 시작시간 기록(?)

print("걸린 시간:",time.time()-start)

