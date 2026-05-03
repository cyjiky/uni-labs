import random
from copy import deepcopy
from math import pi, cos, sin
import tkinter as tk

def generate_matrix(k):
    matrix = [[0] * col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            val = random.uniform(0, 2.0) * k
            if val < 1.0:
                matrix[i][j] = 0
            else:
                matrix[i][j] = 1
    return matrix

def print_matrix(matrix, name):
    print(f'\n {name}')
    for r in matrix:
        print(*r)

random.seed(5117)

col = 11
row = 11
X_c = 400
Y_c = 400
R = 200
translation = 800
translation_cond = 1600

k_val = 0.695 
A_dir = generate_matrix(k_val)

A_undir = deepcopy(A_dir)
for i in range(row):
    for j in range(col):
        if A_dir[i][j] == 1:
            A_undir[i][j] = 1
            A_undir[j][i] = 1

coord = []
for i in range(10):
    angle = (2 * pi / 10) * i

    x = X_c + R * cos(angle)
    y = Y_c + R * sin(angle)

    coord.append((int(x), int(y)))

coord.append((X_c, Y_c))

print_matrix(A_dir, "A_dir")
print_matrix(A_undir, "A_undir")

out_degrees = [sum(r) for r in A_dir]
in_degrees = [
    sum(A_dir[r][c] for r in range(row)) 
    for c in range(col)
]
undir_degrees = [sum(r) for r in A_undir]
vertices = [
    i for i, d in enumerate(undir_degrees) if d == 1
]
_vertices = [
    i for i, d in enumerate(undir_degrees) if d == 0
]
is_regular = len(set(undir_degrees)) == 1

print(f"out_degrees: {out_degrees}")
print(f"in_degrees: {in_degrees}")
print(f"undir_degrees: {undir_degrees}")
print(f"hanging vertices: {vertices if vertices else None}")
print(f"isolated vertices: {_vertices if _vertices else None}")

if is_regular:
    print("Is regular")
else:
    print("Is not regular")

k_new = 0.75 
A_dir_new = generate_matrix(k_new)
print_matrix(A_dir_new, "A_dir_new")

out_degrees_new = [sum(r) for r in A_dir_new]
in_degrees_new = [
    sum(A_dir_new[r][c] for r in range(row)) for c in range(col)
]
print(f"out_degrees_new: {out_degrees_new}")
print(f"in_degrees_new: {in_degrees_new}")

for i in range(row):
    for k in range(row):
        for j in range(col):
            if A_dir_new[i][k] == 1 and A_dir_new[k][j] == 1:
                print(f"2: {i} - {k} - {j}")

for i in range(row):
    for k in range(row):
        for m in range(row):
            for j in range(col):
                if A_dir_new[i][k] == 1 and A_dir_new[k][m] == 1 and A_dir_new[m][j] == 1:
                    print(f"3: {i} - {k} - {m} - {j}")

Reach_mat = deepcopy(A_dir_new)

for i in range(row):
    Reach_mat[i][i] = 1

for k in range(row):
    for i in range(row):
        for j in range(col):
            if Reach_mat[i][k] == 1 and Reach_mat[k][j] == 1:
                Reach_mat[i][j] = 1

print_matrix(Reach_mat, "Reach_mat")

Strong_mat = [[0] * col for _ in range(row)]

for i in range(row):
    for j in range(col):
        if Reach_mat[i][j] == 1 and Reach_mat[j][i] == 1:
            Strong_mat[i][j] = 1

print_matrix(Strong_mat, "Strong_mat")

_dict = {}

for i in range(row):
    row_signature = tuple(Strong_mat[i]) 
    if row_signature not in _dict:
        _dict[row_signature] = []
    _dict[row_signature].append(i)

comp_list = list(_dict.values())
comp_num = 1
for comp in _dict.values():
    print(f"{comp_num}: {comp}")
    comp_num += 1

num_comps = len(comp_list)
A_cond = [[0] * num_comps for _ in range(num_comps)]

for i, comp1 in enumerate(comp_list):
    for j, comp2 in enumerate(comp_list):
        if i != j:
            has_edge = any(
                A_dir_new[u][v] == 1 for u in comp1 for v in comp2
            )
            if has_edge:
                A_cond[i][j] = 1

coord_cond = []
R_cond = 120
for i in range(num_comps):
    if num_comps > 1:
        angle = (2 * pi / num_comps) * i
    else:
        angle = 0
    x = X_c + R_cond * cos(angle)
    y = Y_c + R_cond * sin(angle)
    coord_cond.append((int(x), int(y)))

window = tk.Tk()
window.title("Lab04")

canvas = tk.Canvas(
    window, width=2400, 
    height=800, bg="pink"
)
canvas.pack()

canvas.create_text(
    400, 50, 
    text="A_dir", 
    font=("Arial", 20, "bold")
)
canvas.create_text(
    400 + translation, 
    50, text="A_undir", 
    font=("Arial", 20, "bold")
)

for i in range(row):
    for j in range(col):
        if A_dir[i][j] == 1:
            x1, y1 = coord[i]
            x2, y2 = coord[j]
            canvas.create_line(
                x1, y1, x2, y2, 
                arrow=tk.LAST, 
                fill="red", 
                width=2
            )

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

for i in range(num_comps):
    for j in range(num_comps):
        if A_cond[i][j] == 1:
            x1, y1 = coord_cond[i]
            x2, y2 = coord_cond[j]
            canvas.create_line(
                x1 + translation_cond, y1,
                x2 + translation_cond, y2,
                arrow=tk.LAST,
                fill="blue",
                width=2
            )

r_node = 20
r_cond_node = 25
for i in range(len(coord)):
    x, y = coord[i]

    canvas.create_oval(
        x - r_node,
        y - r_node,
        x + r_node,
        y + r_node,
        fill="white",
        outline="red",
        width=2,
    )
    canvas.create_text(
        x, y, text=str(i), 
        font=("Arial", 15, "bold")
    )

    canvas.create_oval(
        x + translation - r_node,
        y - r_node,
        x + translation + r_node,
        y + r_node,
        fill="white",
        outline="red",
        width=2,
    )
    canvas.create_text(
        x + translation, y, 
        text=str(i), 
        font=("Arial", 15, "bold")
    )

    for i in range(num_comps):
        x, y = coord_cond[i]
        canvas.create_oval(
            x + translation_cond - r_cond_node, y - r_cond_node,
            x + translation_cond + r_cond_node, y + r_cond_node,
            fill="white", outline="blue", width=3,
        )

window.mainloop()
