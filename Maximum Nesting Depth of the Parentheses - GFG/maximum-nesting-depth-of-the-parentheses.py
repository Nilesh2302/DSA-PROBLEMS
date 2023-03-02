#User function Template for python3

class Solution:
    def maxDepth(self, s):
        # Code here
        depth=0
        op = 0 #open
        for p in s: #parenthesis checking
            if p=='(':
                op += 1
            
            if p==')':
                op -= 1
            
            depth = max(depth,op)    
        
        return depth


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        print(ob.maxDepth(s))
# } Driver Code Ends