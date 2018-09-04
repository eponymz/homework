# Structure Definition
#       1    ---
#    /     \   |
#   2 - 4 - 3  |
#    \  |  /   |
#       5    ---

structure = {'1': ['2', '3'], '2': ['4', '5'], '3': ['4', '5'], '4': ['5'], '5': ['1']}
completePath = []


# Recursive depth first search
def recursvieDFS(structure, nodeStart, completePath):
    completePath = completePath + [nodeStart]
    print completePath
    for node in structure[nodeStart]:
        if not node in completePath:
            completePath = recursvieDFS(structure, node, completePath)
    return completePath


print ('Depth First Search', recursvieDFS(structure, '3', completePath))


# Iterative breadth first search
def iterativeBFS(structure, nodeStart, completePath):
    x = [nodeStart]
    while x:
        print x
        firstNode = x.pop(0)
        if not firstNode in completePath:
            completePath = completePath + [firstNode]
            x = x + structure[firstNode]
    return completePath


print ('Breadth First Search', iterativeBFS(structure, '3', completePath))
