class Solution:
    
#     def findPeakElement(self, arr):
#         n=len(arr)
#         s = 0
#         e = n-1
        
        
#         while s<=e:
#             mid = (s+e)//2
#             if (mid==0 or arr[mid]>=arr[mid-1]) and (mid==n-1 or arr[mid]>=arr[mid+1]):
#                 return mid
            
#             elif mid>0 and  arr[mid]<arr[mid-1]:
#                 e = mid-1
                
            
#             elif mid<n-1 and arr[mid]<arr[mid+1]:
#                 s = mid+1
    def findPeakElement(self, arr: List[int]) -> int:
        n=len(arr)
        s=0
        e=n-1
        while s<=e:
            mid = s+(e-s)//2
            if(mid==0 or arr[mid]>=arr[mid-1]) and (mid==n-1 or arr[mid]>=arr[mid+1]):
                return mid
            
            elif (mid>0 and arr[mid]<arr[mid-1]):
                e = mid-1
            
            elif (mid<n-1 and arr[mid]<arr[mid+1]):
                s = mid+1
                