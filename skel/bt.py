
nodes = []

def dfs(n, edges):
    global nodes

    #TODO do a depth first search and add n to nodes

def tree_traversal(n, edges):
    global nodes
    nodes.append(n)

    dfs(n, edges)

    return nodes
