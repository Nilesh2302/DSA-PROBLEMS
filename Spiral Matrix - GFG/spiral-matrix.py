#User function Template for python3

# You are required to complete this fucntion
# Function should return an integer
class Solution:
    def findK(self, a, n, m, k):
        # Your code goes here
        strow = 0
        stcol = 0
        enrow = n-1
        encol = m-1
        cnt = 0
        while cnt<=k:
            for i in range(stcol,encol+1):
                ans = a[strow][i]
                cnt+=1
                if cnt==k:
                    return ans
            
            strow+=1
            
            for i in range(strow,enrow+1):
                ans = a[i][encol]
                cnt+=1
                if cnt==k:
                    return ans
            
            encol-=1
            
            for i in range(encol,stcol-1,-1):
                ans = a[enrow][i]
                cnt+=1
                if cnt==k:
                    return ans
            
            enrow-=1
            
            for i in range(enrow,strow-1,-1):
                ans = a[i][stcol]
                cnt+=1
                if cnt==k:
                    return ans
            
            stcol+=1      
                



#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[1])]for j in range(n[0])]
        c=0
        for i in range(n[0]):
            for j in range(n[1]):
                matrix[i][j] = arr[c]
                c+=1
        obj = Solution()
        print(obj.findK(matrix, n[0], n[1], n[2]))

# } Driver Code Ends