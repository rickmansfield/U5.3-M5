"""
WARNING... I could not get this version to work
"""
output = 35
def sumRangeInBST(root, lower, upper):
    sum = 0
    
    if root != None:
        if lower <= root.value and root.value <= upper:
            sum += root.value
            
        if lower <= root.value:
            sum += sumRangeInBST(root.left, lower, upper)
            
        if root.value <= upper:
            sum += sumRangeInBST(root.right, lower, upper)
        
    return sum

"""
root = [11, 6, 16, 4, 8, null, 19]
lower 8 
upper 16

     11
     /\
    6  16
   /\   \
  4  8   19
"""