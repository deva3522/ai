graph = {
  '1': ['2', '3', '4'],
  '2': ['4', '5'],
  '3': ['4'],
  '4': [],
  '5': []
}

visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print('DFS')
dfs(visited, graph, '1')
