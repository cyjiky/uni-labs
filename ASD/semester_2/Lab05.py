import random
from math import pi, cos, sin
import tkinter as tk

random.seed(5117)

col = 11
row = 11
X_c = 400
Y_c = 400
R = 200
translation = 800

A_dir = [[0] * col for _ in range(row)]
coord = []

for i in range(row):
    for j in range(col):
        val = random.uniform(0, 2.0) * 0.695
        if val < 1.0:
            A_dir[i][j] = 0
        else:
            A_dir[i][j] = 1

for i in range(10):
    angle = (2 * pi / 10) * i
    x = X_c + R * cos(angle)
    y = Y_c + R * sin(angle)
    coord.append((int(x), int(y)))
coord.append((X_c, Y_c))


def bfs_generator():
    visited = [False] * row
    states = ["white"] * row
    tree_edges = []

    while True:
        start_node = None
        for i in range(row):
            if not visited[i] and any(A_dir[i][j] == 1 for j in range(col)):
                start_node = i
                break

        if start_node is None:
            yield states, tree_edges
            break

        queue = [(start_node, None)]
        visited[start_node] = True
        states[start_node] = "pink"
        yield states, tree_edges

        while queue:
            curr, parent = queue.pop(0)
            if parent is not None:
                tree_edges.append((parent, curr))

            yield states, tree_edges

            for j in range(col):
                if A_dir[curr][j] == 1 and not visited[j]:
                    visited[j] = True
                    states[j] = "red"
                    queue.append((j, curr))
                    yield states, tree_edges

            states[curr] = "pink"
            yield states, tree_edges


def dfs_generator():
    visited = [False] * row
    states = ["white"] * row
    tree_edges = []

    def dfs_recursive(node, parent):
        visited[node] = True
        states[node] = "red"
        if parent is not None:
            tree_edges.append((parent, node))
        yield states, tree_edges

        for j in range(col):
            if A_dir[node][j] == 1 and not visited[j]:
                yield from dfs_recursive(j, node)

        states[node] = "pink"
        yield states, tree_edges

    while True:
        start_node = None
        for i in range(row):
            if not visited[i] and any(A_dir[i][j] == 1 for j in range(col)):
                start_node = i
                break

        if start_node is None:
            yield states, tree_edges
            break

        yield from dfs_recursive(start_node, None)


class GraphTraversalApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Lab05")

        self.canvas = tk.Canvas(window, width=1600, height=800, bg="pink")
        self.canvas.pack()

        self.btn_bfs = tk.Button(
            window,
            text="BFS ",
            font=("Arial", 14),
            command=self.step_bfs,
            bg="lightpink",
        )
        self.btn_bfs.place(x=300, y=720)

        self.btn_dfs = tk.Button(
            window,
            text="DFS",
            font=("Arial", 14),
            command=self.step_dfs,
            bg="lightpink",
        )
        self.btn_dfs.place(x=1100, y=720)

        self.bfs_gen = bfs_generator()
        self.dfs_gen = dfs_generator()

        self.bfs_states = ["white"] * row
        self.bfs_tree = []

        self.dfs_states = ["white"] * row
        self.dfs_tree = []

        self.bfs_clicks = 0
        self.dfs_clicks = 0
        self.bfs_log = f"Count: {self.bfs_clicks}"
        self.dfs_log = f"Count: {self.dfs_clicks}"

        self.window.bind("<Left>", lambda event: self.step_bfs())
        self.window.bind("<Right>", lambda event: self.step_dfs())

        self.draw_all()

    def step_bfs(self):
        self.bfs_clicks += 1
        try:
            self.bfs_states, self.bfs_tree = next(self.bfs_gen)
            self.bfs_log = f"Count: {self.bfs_clicks}"
        except StopIteration:
            self.bfs_log = f"End"
        self.draw_all()

    def step_dfs(self):
        self.dfs_clicks += 1
        try:
            self.dfs_states, self.dfs_tree = next(self.dfs_gen)
            self.dfs_log = f"Count: {self.dfs_clicks}"
        except StopIteration:
            self.dfs_log = f"End"
        self.draw_all()

    def draw_all(self):
        self.canvas.delete("all")

        self.canvas.create_text(
            400,
            50,
            text=f"BFS {self.bfs_log}",
            font=("Arial", 20, "bold"),
            fill="black",
        )
        self.canvas.create_text(
            400 + translation,
            50,
            text=f"DFS {self.dfs_log}",
            font=("Arial", 20, "bold"),
            fill="black",
        )

        self.draw_graph(0, self.bfs_states, self.bfs_tree)
        self.draw_graph(translation, self.dfs_states, self.dfs_tree)

    def draw_graph(self, offset, states, tree_edges):
        for i in range(row):
            for j in range(col):
                if A_dir[i][j] == 1:
                    x1, y1 = coord[i]
                    x2, y2 = coord[j]
                    self.canvas.create_line(
                        x1 + offset,
                        y1,
                        x2 + offset,
                        y2,
                        arrow=tk.LAST,
                        fill="pink",
                        width=1,
                    )

        for u, v in tree_edges:
            x1, y1 = coord[u]
            x2, y2 = coord[v]
            self.canvas.create_line(
                x1 + offset, y1, x2 + offset, y2, arrow=tk.LAST, fill="black", width=4
            )

        r_node = 20
        for i in range(len(coord)):
            x, y = coord[i]
            color = states[i]

            self.canvas.create_oval(
                x + offset - r_node,
                y - r_node,
                x + offset + r_node,
                y + r_node,
                fill=color,
                outline="black",
                width=2,
            )
            text_color = "white" if color == "gray" else "black"
            self.canvas.create_text(
                x + offset, y, text=str(i), font=("Arial", 15, "bold"), fill=text_color
            )


if __name__ == "__main__":
    window = tk.Tk()
    app = GraphTraversalApp(window)
    window.mainloop()
