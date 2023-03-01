#User function Template for python3

class Solution:
    def findMin(self, arr, n):
        #complete the function here
        s,e = 0,n-1
        while s<e:
            mid = (s+e)//2
            
            if arr[mid]<arr[e]:   #things depend on that if the arrr of mid is greater or smaller than arr mid
                e = mid           # if it is smaller than the end then end becomes the mid
                
            elif arr[mid]>arr[e]: # else s is mid+1
                s = mid+1
            
            else:
                e = mid - 1
        
        return arr[s]        
                
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.findMin(arr, n))
# } Driver Code Ends