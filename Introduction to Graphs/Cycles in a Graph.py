graph = {}

while True:
    node = input().split("-")

    if node[0] == "End":
        break

    if node[0] not in graph.keys():
        graph[node[0]] = []

    if node[1] not in graph.keys():
            graph[node[1]] = []

    graph[node[0]].append(node[1])



def createConnectedGraph(graph):
    connectedGraph = {}

    for node, children in graph.items():

        if node not in connectedGraph:
            connectedGraph[node] = 0

        for child in children:

            if child not in connectedGraph:
                connectedGraph[child] = 1
            else:
                connectedGraph[child] += 1

    return connectedGraph

connectedGraph = createConnectedGraph(graph)



def findNotConnected(connectedGraph):

    for node, connections in connectedGraph.items():

        if connections == 0:
            return node

    return None

has_cycle = False

while connectedGraph:
    notConnected = findNotConnected(connectedGraph)

    if notConnected == None:
        has_cycle = True
        break


    for node in graph[notConnected]:
        connectedGraph[node] -= 1

    del connectedGraph[notConnected]

if has_cycle:
    print("Acyclic: No")
else:
    print("Acyclic: Yes")