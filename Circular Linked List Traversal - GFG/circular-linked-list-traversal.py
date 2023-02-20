class Node: 
      
    # Constructor to create  a new node 
    def __init__(self, data): 
        self.data = data  
        self.next = None
  
class CircularLinkedList: 
      
    # Constructor to create a empty circular linked list 
    def __init__(self): 
        self.head = None
  
    # Function to insert a node at the beginning of a 
    # circular linked list 
    def push(self, data): 
        ptr1 = Node(data)
        ptr1.data=data
        temp = self.head 
          
        ptr1.next = self.head 
  
        # If linked list is not None then set the next of 
        # last node 
        if self.head is not None: 
            while(temp.next != self.head): 
                temp = temp.next 
            temp.next = ptr1 
  
        else: 
            ptr1.next = ptr1 # For the first node 
  
        self.head = ptr1  
  
    # Function to print nodes in a given circular linked list 
    def printList(self): 
        curr = self.head.next
        print(self.head.data,end=' ')
        while curr!= self.head:
            print(curr.data,end=' ')
            curr = curr.next
        
        # Write your code here
        return
        


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        cllist = CircularLinkedList()
        l=list(map(int,input().strip().split()))
        for i in range(0,len(l)):
            cllist.push(l[i])
        cllist.printList()
        print()
# } Driver Code Ends