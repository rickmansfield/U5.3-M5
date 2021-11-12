Ha, Tom and Michael and I worked on this very problem over and over until l got it.

The problem requires initializing "current" to the head node. Then initializing variables to track both the "previous" and "next" data positions in the singly linked list.

This particular solution is "iterative" using a while loop the code systematically identifies the "newNext" position so the data is not lost. Sequentially we reverse the "next" pointer to the previous node and then identify the "new" previous. This permits reassigning current from the original point to the next node in the list. This process continues until the current node is "None" at which time the loop is complete and the block returns the previous or "prev" in this case node as it is now the head node.

FYI... I had to set up a chart.drawio file and work this out visually over and over before I could reproduce its code.

There is a recursive solution but I studied the "iterative" version the most and felt stronger reproducing it. That said I think this code block could have worked too.

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