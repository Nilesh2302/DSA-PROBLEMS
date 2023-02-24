#User function Template for python3

def firstocc(arr,n,x):
    s = 0
    e = n-1
    ans=-1
    
    while s<=e:
        mid = (s+e)//2
        if arr[mid]==x:
            ans = mid
            e = mid-1
        
        elif x >arr[mid]:
            s = mid + 1
        
        elif x < arr[mid]:
            e = mid-1
    
    return ans

def lastocc(arr,n,x):
    s = 0
    e = n-1
    ans=-1
    
    while s<=e:
        mid = (s+e)//2
        if arr[mid]==x:
            ans = mid
            s = mid+1
        
        elif x >arr[mid]:
            s = mid + 1
        
        elif x < arr[mid]:
            e = mid-1
            
    
        
    
    return ans    
    
    
    
        
            
            

def find(arr,n,x):
    # code here
    first = firstocc(arr,n,x)
    last = lastocc(arr,n,x)
    
    return first,last
    
    



#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ans=find(arr,n,x)
    print(*ans)
# } Driver Code Ends