#TurtleDraw.py
import turtle as t
t.bgcolor("black")
colors=['orange','blue','yellow','red','purple','green']
for i in range (360):
    t. pencolor(colors[i%6])
    t.width(i/60)
    t. fd(i)
    t.right(59)
t.done
