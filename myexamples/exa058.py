# 画图，学用rectangle画方形

from tkinter import *

canvas = Canvas(width=600, height=600, bg='green')
canvas.pack(expand=YES, fill=BOTH)
x0 = 263
y0 = 263
y1 = 275
x1 = 275
for i in range(19):
    canvas.create_rectangle(x0, y0, x1, y1, width=1)
    x0 -= 5
    y0 -= 5
    x1 += 5
    y1 += 5
mainloop()
