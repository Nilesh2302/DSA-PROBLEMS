#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n):
        total = n*(n+1)//2
        s1 = set(arr)
        x = total-sum(s1)
        y = sum(arr)-sum(s1)
        return y,x
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # def findTwoElement( self,arr, n): 
    #     # code here
    #     x = 0
    #     y = 0
    #     xor1 = 0
        
    #     # /* Get the xor of all array elements */
    #     for i in range(n):
    #         xor1 = xor1 ^ arr[i]
        
    #     # xor the previous result with the numbers 1 to n
    #     for i in range(1,n+1):
    #         xor1 = xor1 ^ i
        
        
    #     # get the rightmost set bit in set_bit_no
    #     set_bit_no = xor1 and -(xor1-1)
    #     #  Now divide elements into two sets by comparing a rightmost set bit
    # #   of xor1 with the bit at the same position in each element.
    # #   Also, get XORs of two sets. The two XORs are the output elements.
    # #   The following two for loops serve the purpose 
        
    #     for i in range(n):
    #         if arr[i] and set_bit_no:
    #             x = x ^ arr[i]
            
    #         else:
    #             y = y ^ arr[i]
                
        
    #     for i in range(1,n+1):
    #         if i and set_bit_no:
    #             x = x ^ i
            
    #         else:
    #             y = y ^ i
        
    #     # we just check that from x and y whcih is missing and which is repeting number
    #     x_cnt = 0
    #     for i in range(n):
    #         if arr[i]==x:
    #             x_cnt+=1
        
    #     if x_cnt==0:
    #         return [y,x]
        
    #     return [x,y]   
                
            
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends