class Solution:
    def searchInsert(self, Arr: List[int], k: int) -> int:
        N = len(Arr)
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
                
        return e+1 
        