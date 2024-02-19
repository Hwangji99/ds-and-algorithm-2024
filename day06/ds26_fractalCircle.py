# date : 2024-02-19
# file : ds26_fractalCircle.py
# desc :  프랙탈 원 그리기

from tkinter import *
import random

def drawCircle(x,y,r):
    canvas.create_oval(x-r, y-r, x+r, y+r, width=2, outline=random.choice(colors))
    # canvas.create_text(x, y-r, text=str(count), font=('Gullim', 30))
    if r >= 5:
        drawCircle(x-r / 2, y, r // 2)
        drawCircle(x+r / 2, y, r // 2)

# 전역변수
radius = 400
wSize = 1000
colors = ['red', 'green', 'blue', 'black', 'orange', 'indigo', 'violet', 'crimson', 'azure', 'gray']

# 메인코드
window = Tk()
window.title('프랙탈 원그리기')
canvas = Canvas(window, height=wSize, width=wSize, bg='white')

drawCircle(wSize//2, wSize//2, radius)

canvas.pack()

# r = 400
# # cx-r, cy-r(좌측상단 x,y)  # cx+r, cy+r(우측하단 x,y)
# canvas.create_oval(cx-r, cy-r, cx+r, cy+r, width=2, outline='red')

window.mainloop()