graph={5: [2,4], 2: [1,7], 4:[11,45], 1:[], 7:[] , 11: [99], 45:[], 99:[]}

queue=[]
visited=[]

def BFS(graph,queue,visited,node):

    parent={node:None} # initially root node is there no parent of root node as it is the starting point of graph

    queue.append(node)
    visited.append(node)

    while queue: # Till queue is not empty

        m=queue.pop(0) # 5 initially

        print(f"Node: {m}, Parent: {parent[m]}")

        for n in graph[m]: # now neighbours of node
            if n not in visited:
                queue.append(n)
                visited.append(n)
                parent[n]=m

root=5
BFS(graph,queue,visited,root)