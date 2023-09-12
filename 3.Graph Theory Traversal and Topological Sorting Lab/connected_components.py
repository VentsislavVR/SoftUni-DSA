nodes = int(input())
graph = []

for node in range(nodes):
    line = input()
    children = [] if line == '' else [int(x) for x in line.split()]
    graph.append(children)


def dfs(node, graph, visited, component):
    if visited[node]:
        return
    visited[node] = True
    for child in graph[node]:
        dfs(child,graph, visited, component)
    component.append(node)


visited = [False] * nodes
for node in range(nodes):
    if visited[node]:
        continue
    component = []
    dfs(node, graph, visited, component)
    # if component:
    print(f'Connected component: {" ".join([str(x) for x in component])}')

