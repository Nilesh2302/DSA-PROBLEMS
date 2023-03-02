class Solution:
    def maxDepth(self, s: str) -> int:
        depth=0
        op = 0 #open
        for p in s: #parenthesis checking
            if p=='(':
                op += 1
            
            if p==')':
                op -= 1
            
            depth = max(depth,op)    
        
        return depth
        