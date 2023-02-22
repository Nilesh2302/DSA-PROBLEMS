class Solution:
    def nextPermutation(self, arr: List[int]) -> None:
        N = len(arr)
        if N<=2:
            return arr.reverse()
        
        ptr = N-2
        while ptr>=0 and arr[ptr]>=arr[ptr+1]:
            ptr-=1
        
        #means given combination is the last combination is the last combination and
        # next is reversed of it
        if ptr==-1:
            arr.reverse()
            return arr
        
        for i in range(N-1,ptr,-1):
            if arr[ptr]<arr[i]:
                arr[ptr],arr[i] = arr[i],arr[ptr]
                break
        
        arr[ptr+1:] = reversed(arr[ptr+1:])  
        return arr
        """
        Do not return anything, modify nums in-place instead.
        """
        