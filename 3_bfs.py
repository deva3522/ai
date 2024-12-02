graph = {
  '1': ['2', '3', '4'],
  '2': ['4', '5'],
  '3': ['4'],
  '4': [],
  '5': []
}

def bfs(graph, start):
    queue = [start]
    visited = set()
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(graph[node])

print("Breadth First Search Traversal:")
bfs(graph, '1')
