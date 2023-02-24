#User function Template for python3

class Solution:
    
    def binary_search(self,arr, low, high):
        """
        This function performs binary search to check whether the given array is sorted in
        ascending or descending order.
        """
        if low == high:
            return True
    
        mid = (low + high) // 2
        if arr[mid] <= arr[mid+1]:
            return self.binary_search(arr, low, mid) and self.binary_search(arr, mid+1, high)
        else:
            return False
    def arraySortedOrNot(self, arr, n):
        # code here
        s = 0 
        e = n-1
        ans = self.binary_search(arr, s, e)
        return ans
            
        

#{  
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        
        ob = Solution()
        ans = ob.arraySortedOrNot(arr, n)
        if ans:
            print(1)
        else:
            print(0)
        tc -= 1

# } Driver Code Ends