from task4 import *

def colors_gradient(len : int) -> list:
    if len < 1:
        return []
    return ['#%02X%02X%02X' % (int(25.0 + i*(200/len)), int(75.0 + i*(160/len)), int(75.0 + i*(160/len))) for i in range(len)]

def visible_dfs(heap : list):
    '''Visualize Depth-first search in heap'''
    if heap is None or len(heap) == 0:
        return
    root = build_tree(heap_list)
    cg = colors_gradient(len(heap))
    vstack = []
    curr = root
    for i in range(len(heap)):
        curr.color = cg[i]
        draw_tree(root)
        if curr.left:
            if curr.right:
                vstack.append(curr.right)
            curr = curr.left
        elif curr.right:
            curr = curr.right
        elif vstack:
            curr = vstack.pop()
    
def my_bfs(graph, queue, visited=None):
    '''Recursive Breadth-first search'''
    if visited is None:
        visited = set()
    if not queue:
        return
    vertex = queue.popleft()
    if vertex not in visited:
        print(vertex, end=" ")
        visited.add(vertex)
        queue.extend(set(graph[vertex]) - visited)
    my_bfs(graph, queue, visited)

def visible_bfs(heap : list):
    '''Visible Breadth-first search in heap'''
    if heap is None or len(heap) == 0:
        return
    cg = colors_gradient(len(heap))
    root = build_tree(heap)
    cstack = [root]
    i = 0
    while True:
        nstack = []
        while cstack:
            curr = cstack.pop()
            curr.color = cg[i]
            draw_tree(root)
            i += 1
            if curr.left:
                nstack.append(curr.left)
            if curr.right:
                nstack.append(curr.right)
        if not nstack:
            break
        cstack = nstack
        cstack.reverse()

if __name__ == "__main__":
    heap_list = [1,3,5,6,9,4,14,2,1,7]
    heapq.heapify(heap_list)
    
    visible_dfs(heap_list)
    visible_bfs(heap_list)