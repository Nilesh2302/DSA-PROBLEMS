class Solution(object):
    def findNumbers(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt=0
        for i in arr:
            if len(str(i))%2==0:
                   cnt+=1
        
        return cnt
            