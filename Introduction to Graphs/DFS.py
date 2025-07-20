adjArr =  [
    [3, 6],
    [3 ,6, 4, 2, 5],
    [1, 4, 5],
    [5, 1, 0],
    [1, 2, 6],
    [2, 1, 3],
    [0, 1, 4]
]


stack = []

def dfs(node, index, adjArr):

    if index not in stack:
        stack.append(index)

        for childNode in node:
            dfs(adjArr[childNode], childNode, adjArr)

        print(index, end=" ")

for i in  range(len(adjArr)):
    dfs(adjArr[i], i, adjArr)



