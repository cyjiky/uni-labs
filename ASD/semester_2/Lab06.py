import random
from copy import deepcopy
from math import pi, cos, sin, ceil
import tkinter as tk

seed_val = 5117
n1, n2, n3, n4 = 5, 1, 1, 7
k = 1.0 - n3 * 0.01 - n4 * 0.005 - 0.05

col = 11
row = 11
X_c = 400
Y_c = 400
R = 250
translation = 800

class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adj = {i: [] for i in range(num_nodes)}

    def add_node(self, node):
        if node not in self.adj:
            self.adj[node] = []

    def remove_node(self, node):
        if node in self.adj:
            del self.adj[node]
            for u in self.adj:
                self.adj[u] = [(v, w) for v, w in self.adj[u] if v != node]

    def add_edge(self, u, v, weight):
        if not self.has_edge(u, v):
            self.adj[u].append((v, weight))
            self.adj[v].append((u, weight))

    def remove_edge(self, u, v):
        self.adj[u] = [
            (node, weight) for node, weight in self.adj[u] if node != v
        ]
        self.adj[v] = [
            (node, weight) for node, weight in self.adj[v] if node != u
        ]

    def has_edge(self, u, v):
        for node, _ in self.adj[u]:
            if node == v:
                return True
        return False

random.seed(seed_val)

A_dir = [[0] * col for _ in range(row)]
for i in range(row):
    for j in range(col):
        val = random.uniform(0, 2.0) * k
        A_dir[i][j] = 0 if val < 1.0 else 1

A_undir = deepcopy(A_dir)
for i in range(row):
    for j in range(col):
        if A_dir[i][j] == 1:
            A_undir[i][j] = 1
            A_undir[j][i] = 1

random.seed(seed_val)
B = [[random.uniform(0, 2.0) for _ in range(col)] for _ in range(row)]

C = [[0] * col for _ in range(row)]
D = [[0] * col for _ in range(row)]
H = [[0] * col for _ in range(row)]
Tr = [[0] * col for _ in range(row)]
W = [[0] * col for _ in range(row)]

for i in range(row):
    for j in range(col):
        C[i][j] = ceil(B[i][j] * 100 * A_undir[i][j])
        D[i][j] = 1 if C[i][j] > 0 else 0

for i in range(row):
    for j in range(col):
        H[i][j] = 1 if D[i][j] != D[j][i] else 0
        Tr[i][j] = 1 if i < j else 0

for i in range(row):
    for j in range(col):
        if i < j:
            weight = (D[i][j] + H[i][j] * Tr[i][j]) * C[i][j]
            W[i][j] = weight
            W[j][i] = weight

main_graph = Graph(row)
for i in range(row):
    for j in range(i + 1, col):
        if W[i][j] > 0:
            main_graph.add_edge(i, j, W[i][j])

coord = []
for i in range(10):
    angle = (2 * pi / 10) * i
    x = X_c + R * cos(angle)
    y = Y_c + R * sin(angle)
    coord.append((int(x), int(y)))
coord.append((X_c, Y_c))

window = tk.Tk()
window.title("Lab06")

canvas = tk.Canvas(window, width=1600, height=800, bg="pink")
canvas.pack()

for i in range(row):
    for j in range(i + 1, col):
        if W[i][j] > 0:
            x1, y1 = coord[i]
            x2, y2 = coord[j]
            canvas.create_line(
                x1, y1, x2, y2, 
                fill="black", width=1
            )
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            canvas.create_rectangle(
                mx-10, my-8, 
                mx+10, my+8, 
                fill="white", 
                outline="white"
            )
            canvas.create_text(
                mx, my, 
                text=str(W[i][j]), 
                fill="blue", 
                font=("Arial", 10)
            )

r_node = 20
def draw_nodes(offset):
    for i in range(len(coord)):
        x, y = coord[i]
        x += offset
        canvas.create_oval(
            x - r_node, y - r_node, 
            x + r_node, y + r_node, 
            fill="white", 
            outline="black", 
            width=2
        )
        canvas.create_text(
            x, y, 
            text=str(i), 
            font=("Arial", 14, "bold")
        )

draw_nodes(0)
draw_nodes(translation)

visited_nodes = {0}
unvisited_nodes = set(range(1, row))
total_mst_weight = 0

def prim_step(event=None):
    global total_mst_weight
    if not unvisited_nodes:
        canvas.create_text(
            400 + translation, 750, 
            text=f"Total Weight: {total_mst_weight}", 
            font=("Arial", 16, "bold"), 
            fill="green"
        )
        return
    
    min_weight = float('inf')
    best_edge = None

    for u in visited_nodes:
        for v, weight in main_graph.adj[u]:
            if v in unvisited_nodes and weight < min_weight:
                min_weight = weight
                best_edge = (u, v, weight)

    if best_edge:
        u, v, weight = best_edge
        visited_nodes.add(v)
        unvisited_nodes.remove(v)
        total_mst_weight += weight

        x1, y1 = coord[u]
        x2, y2 = coord[v]
        x1 += translation
        x2 += translation
        
        canvas.create_line(
            x1, y1, x2, y2, 
            fill="red", width=3
        )
        
        draw_nodes(translation)

        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        canvas.create_rectangle(
            mx-12, my-9, mx+12, my+9, 
            fill="yellow", outline="yellow"
        )
        canvas.create_text(
            mx, my, 
            text=str(weight), 
            fill="black", 
            font=("Arial", 12, "bold")
        )

btn = tk.Button(
    window, 
    text="Next", 
    command=prim_step, 
    font=("Arial", 14), 
    bg="lightgreen"
)
btn.pack(pady=10)
window.bind('<space>', prim_step)

window.mainloop()