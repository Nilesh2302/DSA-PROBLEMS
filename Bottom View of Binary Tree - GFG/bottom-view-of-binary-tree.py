#User function Template for python3

class Solution:
    def bottomView(self, root):
        # code here
        if not root:
            return []
    
        # Create a queue of pairs with node and its index
        queue = deque([(root, 0)])
        # Create a map to store the line and the node
        line_map = defaultdict(int)
    
        # Traverse through the tree in level order
        while queue:
            # Store the node and its line number in separate variables
            node, line = queue.popleft()
    
            # Update the map with the current node's value for its line
            line_map[line] = node.data
    
            # Store the left child and its line number in the queue
            if node.left:
                queue.append((node.left, line - 1))
    
            # Store the right child and its line number in the queue
            if node.right:
                queue.append((node.right, line + 1))
    
        # Sort the line map by the line numbers in ascending order
        sorted_map = sorted(line_map.items(), key=lambda x: x[0])
    
        # Return a list of the bottom view nodes
        return [data for line, data in sorted_map]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(50000)
#Contributed by Sudarshan Sharma
from collections import deque
from collections import defaultdict
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ob = Solution()
        res = ob.bottomView(root)
        for i in res:
            print (i, end = " ")
        print()


# } Driver Code Ends