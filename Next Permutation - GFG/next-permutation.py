#User function Template for python3

class Solution:
    def nextPermutation(self, N, arr):
        # code here
        if N<=2:
            return arr.reverse()
        
        ptr = N-2
        while ptr>=0 and arr[ptr]>=arr[ptr+1]:
            ptr -= 1
        
        if ptr == -1:   #means it is the last combination and its reverse is first
            arr.reverse()
            return arr
            
        for i in range(N-1,ptr,-1):
            if arr[ptr]<arr[i]:
                arr[ptr],arr[i] = arr[i],arr[ptr]
                break
        
        arr[ptr+1:] = reversed(arr[ptr+1:])        
        return arr    
               
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        ans = ob.nextPermutation(N, arr)
        for i in range(N):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends