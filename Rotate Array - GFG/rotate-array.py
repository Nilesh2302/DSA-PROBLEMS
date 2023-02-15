#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,arr,k,n):
        #Your code here
        k=k%n 
        st=0
        en=k-1
        while(st<=en):
            arr[st],arr[en]=arr[en],arr[st]
            st+=1
            en-=1
            
        st=k
        en=n-1
        while(st<=en):
            arr[st],arr[en]=arr[en],arr[st]
            st+=1
            en-=1
            
        arr.reverse()


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
def main():
    T=int(input())
    
    while(T>0):
        nd=[int(x) for x in input().strip().split()]
        N=nd[0]
        D=nd[1]
        A=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.rotateArr(A,D,N)
        
        for i in A:
            print(i,end=" ")
            
        print()
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends