#User function Template for python3

class Solution:
    def Solve(self, n, arr):
        # Code here
        cand1,count1 = None,0
        cand2,count2 = None,0
        
        for i in arr:
            if cand1 == i:
                count1 += 1
            
            elif cand2 == i:
                count2 += 1
            
            elif count1 == 0:
                cand1 = i
                count1 += 1
            
            elif count2 == 0:
                cand2 = i
                count2 += 1
            else:
                count1,count2 = count1-1,count2-1
        
        #just check for both candidates greater than n/3 or not
        l1 = [x for x in (cand1,cand2) if arr.count(x)>(n//3)]
        if len(l1)==0:
            l1.append(-1)
            return l1
        
        return l1    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        ob = Solution()
        res = ob.Solve(n, a)
        for val in res:
            print(val, end = ' ')
        print()
# } Driver Code Ends