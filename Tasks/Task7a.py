from collections import deque

def csBinaryTreeInvert(root):
    q = deque()
    q.append(root)
    
    while len(q) > 0:
        p = q.popleft()
        t = p.left
        
        p.left = p.right
        p.right = t
        
        if p.left:
            q.append(p.left)
        
        if p.right:
            q.append(p.right)       
    return root