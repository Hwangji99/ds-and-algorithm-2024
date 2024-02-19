from tkinter import *

## 클래스와 함수 선언 부분 ##
def drawTraining(x, y, size):
    if size >= 30:
        drawTraining(x, y, size/2)
        drawTraining(x+size/2, y, size/2)
        drawTraining(x+size/4, int(y-size*(3**0.5)/4), size/2)
    else:
        canvas.create_polygon(x,y,x+size, y, x+size/2,y-size*(3**0.5)/2,fill='red',outline="red")

## 전역 변수 선언 부분 ##
wSize = 1000
radius = 400

## 메인 코드 부분 ##
window = Tk()
window.title('시에르핀스키 삼각형 모양의 프랙탈')
canvas = Canvas(window, height=wSize, width=wSize, bg='white')

drawTraining(wSize/5, wSize/5*4, wSize*2/3)

canvas.pack()
window.mainloop()