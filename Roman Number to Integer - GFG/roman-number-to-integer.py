#User function Template for python3

class Solution:
    def romanToDecimal(self, s): 
        # code here
        n = len(s)
        
        d = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        
        res = 0
        for i in range(n-1,-1,-1):
            if i<n-1 and d[s[i]]<d[s[i+1]]:
                res-=d[s[i]]
            else:
                res += d[s[i]]
        
        return res       
                
                #{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
# } Driver Code Ends