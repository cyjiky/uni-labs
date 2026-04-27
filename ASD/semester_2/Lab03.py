import random
from copy import deepcopy
from math import pi, cos, sin
import tkinter as tk

random.seed(5117)

col = 11
row = 11
X_c = 400
Y_c = 400
R = 200
translation = 800

A_dir = [[None] * col for i in range(row)]
coord = []

for i in range(row):
    for j in range(col):
        val = random.uniform(0, 2.0) * 0.695

        if val < 1.0:
            A_dir[i][j] = 0
        else:
            A_dir[i][j] = 1

A_undir = deepcopy(A_dir)
for i in range(row):
    for j in range(col):
        if A_dir[i][j] == 1:
            A_undir[i][j] = 1
            A_undir[j][i] = 1

for i in range(10):
    angle = (2 * pi / 10) * i

    x = X_c + R * cos(angle)
    y = Y_c + R * sin(angle)

    coord.append((int(x), int(y)))

coord.append((X_c, Y_c))

print(" A_dir: ")
for r in A_dir:
    print(*r)

print(" A_undir: ")
for r in A_undir:
    print(*r)

window = tk.Tk()
window.title("Lab03")

canvas = tk.Canvas(window, width=1600, height=800, bg="pink")
canvas.pack()

canvas.create_text(400, 50, text="A_dir", font=("Arial", 20, "bold"))
canvas.create_text(400 + translation, 50, text="A_undir", font=("Arial", 20, "bold"))

for i in range(row):
    for j in range(col):
        if A_dir[i][j] == 1:
            x1, y1 = coord[i]
            x2, y2 = coord[j]
            canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST, fill="red", width=2)

        if A_undir[i][j] == 1 and i <= j:
            x1, y1 = coord[i]
            x2, y2 = coord[j]
            canvas.create_line(
                x1 + translation,
                y1,
                x2 + translation,
                y2,
                fill="red",
                width=2,
            )

r_node = 20
for i in range(len(coord)):
    x, y = coord[i]

    canvas.create_oval(
        x - r_node,
        y - r_node,
        x + r_node,
        y + r_node,
        # fill="white",
        outline="red",
        width=2,
    )
    canvas.create_text(x, y, text=str(i), font=("Arial", 15, "bold"))

    canvas.create_oval(
        x + translation - r_node,
        y - r_node,
        x + translation + r_node,
        y + r_node,
        fill="white",
        outline="red",
        width=2,
    )
    canvas.create_text(x + translation, y, text=str(i), font=("Arial", 15, "bold"))

window.mainloop()
