
class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
        


n1 = Node(10)


print(n1.data)
print(n1.next)

print(n1)

n2 = Node(20)

n1.next = n2

print(n1.next)
