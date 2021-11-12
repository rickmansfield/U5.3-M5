def csBSTRangeSum(root, lower, upper):
    sum = 0
        
    if root.left is None and root.right is None and root.value in range (lower, upper +1):
        return root.value
        
    if root is not None and root.value in range(lower, upper + 1):
        sum += root.value
        
    if root.left is not None:
        sum += csBSTRangeSum(root.left, lower, upper)
        
    if root.right is not None:
        sum += csBSTRangeSum(root.right, lower, upper)
    return sum
