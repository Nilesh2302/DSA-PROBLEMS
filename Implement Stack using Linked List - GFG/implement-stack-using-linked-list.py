class StackNode:

    # Constructor to initialize a node
    def __init__(self, data):
        self.data = data
        self.next = None

class MyStack:
    #Function to push an integer into the stack.
    def __init__(self):
        self.head = None
    def push(self, data):
        node = StackNode(data)
        if self.head is None:
            self.head = node
        
        else:
            node.next = self.head
            self.head = node
        
           


    #Function to remove an item from top of the stack.
    def pop(self):
        if self.head is None:
            return -1
        
        else:
            temp = self.head
            self.head = self.head.next
            return temp.data
        
            

        # Add code here



#{ 
 # Driver Code Starts


class StackNode:

    # Constructor to initialize a node
    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = MyStack()
        q = int(input())
        q1 = list(map(int, input().split()))
        i = 0
        while(i < len(q1)):
            if(q1[i] == 1):
                s.push(q1[i + 1])
                i = i + 2
            elif(q1[i] == 2):
                print(s.pop(), end=" ")
                i = i + 1
            elif(s.isEmpty()):
                print(-1)
        print()

# } Driver Code Ends