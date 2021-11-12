def csBinaryTreeInvert(root):

    def nodes(node):
        if not node:
            return
        nodes(node.left)    
        nodes(node.right)
        node.left, node.right = node.right, node.left
    
    
    nodes(root)
    return root 