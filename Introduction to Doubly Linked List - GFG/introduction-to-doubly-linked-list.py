#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
	        self.prev = None
'''
class Solution:
    def constructDLL(self, arr):
        # Code here
        head = Node(arr[0])
        head.next = None
        head.prev = None
        curr = head
        for i in range(1,len(arr)):
            temp = Node(arr[i])
            curr.next = temp
            temp.prev = curr
            curr = curr.next
        
        return head    
    

#{ 
 # Driver Code Starts.
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.prev = None

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.constructDLL(arr)
        while res:
            print(res.data, end = ' ')
            res = res.next
        print()
# } Driver Code Ends