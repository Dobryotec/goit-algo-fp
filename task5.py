import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


class Node:
    def __init__(self, key, color="#FFFFFF"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color 
        self.id = str(uuid.uuid4()) 


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, title="Binary Tree"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors,
            font_color='black', font_size=10, font_weight='bold')
    plt.title(title)
    plt.show()


def build_min_heap(arr):
    nodes = [Node(key) for key in arr]
    n = len(nodes)
    for i in range(n//2 - 1, -1, -1):
        min_heapify(nodes, n, i)
    for i in range(n//2):
        if 2 * i + 1 < n:
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < n:
            nodes[i].right = nodes[2 * i + 2]
    return nodes[0]


def min_heapify(nodes, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and nodes[left].val < nodes[smallest].val:
        smallest = left
    if right < n and nodes[right].val < nodes[smallest].val:
        smallest = right

    if smallest != i:
        nodes[i], nodes[smallest] = nodes[smallest], nodes[i]
        min_heapify(nodes, n, smallest)


def generate_colors(n):
    base_color = mcolors.to_rgb("#1296F0")
    colors = []
    for i in range(n):
        factor = 1 - i / (n + 1)  
        color = (base_color[0] * factor, base_color[1] * factor, base_color[2] * factor)
        colors.append(mcolors.to_hex(color))
    return colors


def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def bfs(root):
    queue = [root]
    node_count = count_nodes(root)
    colors = generate_colors(node_count)
    index = 0

    while queue:
        node = queue.pop(0)
        node.color = colors[index]
        index += 1

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

        draw_tree(root, title=f"BFS Step {index}")


def dfs(root):
    stack = [root]
    node_count = count_nodes(root)
    colors = generate_colors(node_count)
    index = 0

    while stack:
        node = stack.pop()
        node.color = colors[index]
        index += 1

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

        draw_tree(root, title=f"DFS Step {index}") 



arr = [3, 1, 6, 5, 2, 4]

heap_root = build_min_heap(arr)

print("Обхід в ширину (BFS):")
bfs(heap_root)

heap_root = build_min_heap(arr)

print("Обхід в глибину (DFS):")
dfs(heap_root)

