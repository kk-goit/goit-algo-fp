import uuid
import matplotlib.pyplot as plt

import networkx as nx
import heapq

class Node:
  def __init__(self, key, color="skyblue"):
    self.left = None
    self.right = None
    self.val = key
    self.color = color # Додатковий аргумент для зберігання кольору вузла
    self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
  if node is not None:
    graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
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


def draw_tree(tree_root):
  tree = nx.DiGraph()
  pos = {tree_root.id: (0, 0)}
  tree = add_edges(tree, tree_root, pos)

  colors = [node[1]['color'] for node in tree.nodes(data=True)]
  labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

  plt.figure(figsize=(8, 5))
  nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
  plt.show()


def build_tree(heap: list) -> Node | None:
  '''build Tree object from heap list'''
  if len(heap) == 0:
    return None
  root = Node(heap[0])
  lstack = [root]
  i = 1
  l = 1
  while i < len(heap):
    nstack = []
    for _ in range(0, 2**l, 2):
        nroot = lstack.pop()
        nroot.left = Node(heap[i])
        i += 1
        if i == len(heap):
          return root
        nstack.append(nroot.left)
        nroot.right = Node(heap[i])
        i += 1
        if i == len(heap):
          return root
        nstack.append(nroot.right)
    lstack = nstack
    lstack.reverse()
    l += 1
  return root


if __name__ == "__main__":
    # Відображення дерева
    heap_list = [1,3,5,6,9,2,4,14,2,1,2]
    heapq.heapify(heap_list)
    draw_tree(build_tree(heap_list))

