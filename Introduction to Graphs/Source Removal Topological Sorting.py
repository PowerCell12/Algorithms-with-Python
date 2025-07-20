lines = int(input())

graph = {}

for i in range(lines):
    node = input().split(" ->")

    if node[1] == "":
        graph[node[0]] = []
        continue

    related = node[1].strip().split(", ")
    graph[node[0]] = related


def find_dependencies(graph):
    dependencies_by_node = {}

    for node, values in graph.items():

        if node not in dependencies_by_node:
            dependencies_by_node[node] = 0

        for value in values:

            if value in dependencies_by_node.keys():
                dependencies_by_node[value] += 1
            else:
                dependencies_by_node[value] = 1

    return dependencies_by_node

dependencies_by_node = find_dependencies(graph)

stack = []
has_cycles = False

def find_node_without_dep(dependencies_by_node):

    for node, howMany in dependencies_by_node.items():

        if howMany == 0:
            return node

    return None

while dependencies_by_node:
    node_to_remove = find_node_without_dep(dependencies_by_node)

    if node_to_remove is None:
        has_cycles = True
        break

    for child in graph[node_to_remove]:
        dependencies_by_node[child] -= 1

    stack.append(node_to_remove)
    del dependencies_by_node[node_to_remove]


if not has_cycles:
    print(f"Topological sorting: {', '.join(stack)}")
else:
    print("Invalid topological sorting")