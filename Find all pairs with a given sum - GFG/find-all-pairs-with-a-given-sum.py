#User function Template for python3

class Solution:
    def BinarySearch(self,arr,x):
        s=0
        e=len(arr)-1
        while s<=e:
            mid = s + (e-s)//2
            
            if arr[mid]==x:
                return mid
            
            elif x>arr[mid]:
                s = mid+1
            
            elif x<arr[mid]:
                e = mid-1
        
        return -1        
    
        
    def allPairs(self, A, B, N, M, X):
        # Your code goes here 
        lt = []
        B.sort()
        for i in range(N):
            x = X-A[i]
            ans = self.BinarySearch(B,x)
            if ans!= -1:
                lt.append((A[i],B[ans]))
            
        
        lt.sort()
        return lt
            
            
            
        
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        N, M, X = sz[0], sz[1], sz[2]
        A = [int(x) for x in input().strip().split()]
        B = [int(x) for x in input().strip().split()]
        ob=Solution()
        answer = ob.allPairs(A, B, N, M, X)
        sz = len(answer)
        
        if sz==0 :
        	print(-1) 
        
        else: 
            
        	for i in range(sz):
        		if i==sz-1:
        		    print(*answer[i])
        		else:
        		    print(*answer[i], end=', ')
        

        T -= 1


if __name__ == "__main__":
    main()




# } Driver Code Ends