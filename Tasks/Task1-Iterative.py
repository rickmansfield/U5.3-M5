
"""
1. save new "next" pointer (tie)
2. reverse old "next" pointer (untie)
3. move previous ahead
4. move current
"""
def reversedLinkedList(r):
    prev = None
    cur = r # usually the head
    tag = None

    while cur is not None:
        tag = cur.next
        cur.next = prev
        prev = cur
        cur = tag
        
    return prev


def print_helper(self, node, name):
    if node is None:
        print(name + ": None")
    else:
        print(name +":" + node.data)
        
# print(reversedLinkedList([1, 2, 3, 4, 5])) 