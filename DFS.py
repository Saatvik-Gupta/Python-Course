'''
        A
      / | \
     B  C  D
    / \    |
   E   F   G
'''

tree={'A': ['B','C','D'], 'B':['E','F'] , 'C':[],'D':['G'],'E':[],'F':[],'G':[]}
visited=set()
stack=[]
result=[]

print("Graph traversal using DFS Algorithm:\n")

def DFS(tree,visited,stack,node):

    stack.append(node)
    visited.add(node)

    while(stack):

        m=stack.pop()
        result.append(m)

        for n in reversed(tree[m]): # neighbours push when m pop
            if n not in visited:
                stack.append(n)
                visited.add(n)

root_element='A'
DFS(tree,visited,stack,root_element)

print('->'.join(result))

