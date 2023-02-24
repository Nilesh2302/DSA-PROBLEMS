# your task is to complete this function
# function should return index to the any valid peak element
# soln 1: linear traversal
# class Solution:   
#     def peakElement(self,arr, n):
#         # Code here
#         for i in range(n):
#             if (i==0 or arr[i]>=arr[i-1] ) and (i==n-1 or arr[i]>=arr[i+1]):
#                 return i


# slon2 : using binary search
def peakElement(self,arr, n):
        # Code here
        s = 0
        e = n-1
        
        
        while s<=e:
            mid = (s+e)//2
            if (mid==0 or arr[mid]>=arr[mid-1]) and (mid==n-1 or arr[mid]>=arr[mid+1]):
                return mid
            
            elif mid>0 and  arr[mid]<arr[mid-1]:
                e = mid-1
                
            
            elif mid<n-1 and arr[mid]<arr[mid+1]:
                s = mid+1

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        index = Solution().peakElement(arr.copy(), n)
        flag = False
        if index<0 or index>=n:
            flag = False
        else:
            if index == 0 and n==1:
                flag = True
            elif index==0 and arr[index]>=arr[index+1]:
                flag = True
            elif index==n-1 and arr[index]>=arr[index-1]:
                flag = True
            elif arr[index-1] <= arr[index] and arr[index] >= arr[index+1]:
                flag = True
            else:
                flag = False

        if flag:
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends
