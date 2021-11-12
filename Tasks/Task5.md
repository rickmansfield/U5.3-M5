My original UPER:
def csBSTRangeSum(root, lower, upper):
#initialize sum at zero
# confirm root
#if "lower" <= current roots value & right <= "Upper"
# add root value to sum
#start recursive check
#if lower <= roots value
# sum recursively
if lower <= root.value:
#if upper >= current root's value
# sum recursively
but sadly this didn't work. I had to start over. Then I couldn't reason how to write a non-dry version fast enough. So, Im submitting a workable version and will try do DRY it up later.

Also, I was disappointed that I couldn't get this line of code to use for the range...

if lower <= root.value and root.value <= upper:
     do something here....
~~~
Also, I'm still struggling to mentally keep up with where the iterations are. I'm playing around with the Vscode debugger and the python extensions to view the code as it processes but I still haven't mastered stepping through the code with either. 

In the end, I used a recursive process to check each node in more of a depth-first similar process. But since I didn't use a stack and only use a summation I feel like I didn't really apply this week's material very well. 
