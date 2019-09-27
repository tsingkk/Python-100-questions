# 使用 tkinter 画椭圆

from tkinter import *

canvas = Canvas(width=600, height=600, bg='green')
canvas.pack(expand=YES, fill=BOTH)
x0 = 200
y0 = 100
for i in range(10):
    canvas.create_oval(300-x0, 300-y0, 300+x0, 300+y0, width=1)
    x0 -= 10
    y0 -= 5
mainloop()
