lines = int(input())

graph = []

for i in range(lines):

    values = list(map(int, input().split()))

    graph.append(values)

stack = []
printing = []

def dfs(index, graph, stack):

    if index not in stack:

        stack.append(index)

        for childNode in graph[index]:
            dfs(childNode, graph, stack)

        printing.append(index)


for i in range(len(graph)):
    dfs(i, graph, stack)

    if len(printing) > 0:
        print(f"Connected component: {' '.join(list(map(str, printing)))}")
        printing = []
