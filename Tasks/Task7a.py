from collections import deque

def csBinaryTreeInvert(root):
    queue = deque()
    queue.append(root)

    while len(queue) > 0:
        popped = queue.popleft()
        temp = popped.left

        popped.left = popped.right
        popped.right = temp

        if popped.left:
            queue.append(popped.left)
        
        if popped.right:
            queue.append(popped.right)

    return root