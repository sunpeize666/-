'''2023.9.27
손패택(202195056)'''

import turtle as t
t.shape("turtle")

t.penup()
t.goto(-50,-50)
t.pendown()
for i in range(5):
    num = int (t.textinput("도형그리가","몇각형의 도형을 그릴까요"))

    for i in range (num):
        t.forward(100)
        t.left(360/num)

t.done()