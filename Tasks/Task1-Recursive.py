"""
NOTE NOTE NOTE
The solutin starts on line 39
the code before it makes it work in VSCode
"""
class treePaths:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# r = treePaths(5)
# r.left = treePaths(12)
# r.right = treePaths(32)
# r.right.left = treePaths(8)
# r.right.right = treePaths(4)

# r = treePaths(5)
# r.left = treePaths(10)
# r.right = treePaths(25)
# r.right.left = treePaths(12)
# r.right.right = treePaths(3)

# r = treePaths(5)
# r.left = treePaths(6)
# r.right = treePaths(6)
# r.left.left = treePaths(7)
# r.left.right = treePaths(7)
# r.left.left.left = treePaths(8)
# r.left.left.right = treePaths(8)

def reversedLinkedList(r):
    def reversedLinkedList(cur, prev):
        if not cur: 
            return prev
        
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
        return reversedLinkedList(cur, prev)
    
    r = reversedLinkedList(cur = r, prev = None )