class Solution:
    def rearrangeArray(self, arr: List[int]) -> List[int]:
        #User function Template for python3

#User function Template for python3
 


        # code here
        n=len(arr)
        pve = []
        nve = []
        for i in range(n):
            if arr[i]>=0:
                pve.append(arr[i])
            
            else:
                nve.append(arr[i])
        
        arr.clear()   #used to clear/delete the elements from the array
         
        if len(pve)>len(nve):
            length = len(nve)
         
        else:
            length = len(pve)
        
        for i in range(length):
            arr.append(pve[i])
            arr.append(nve[i])
            
        if len(pve)>len(nve):
            for i in range(length,len(pve)):
                arr.append(pve[i])
                
         
        else:
            for i in range(length,len(nve)):
                arr.append(nve[i])
        
        return arr
                 

        