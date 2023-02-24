#User function Template for python3

class Solution:
    def searchInsertK(self, Arr, N, k):
        # code here
        s = 0
        e = N-1
        
        while s<=e:
            mid = (s+e)//2
            
            if k==Arr[mid]:
                return mid
            
            elif k>Arr[mid]:
                s = mid+1
                
            elif k<Arr[mid]:
                e = mid-1
                
        return s        
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        k = int(input())
        ob = Solution()
        print(ob.searchInsertK(Arr, N, k))
# } Driver Code Ends