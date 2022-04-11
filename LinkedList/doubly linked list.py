class Node:
    def __init__(self,value=None):
        self.value=value
        self.prev=None
        self.next=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
    def create(self,value):
        node=Node(value)
        node.next=None
        node.prev=None
        self.head=node
        self.tail=node
        return "created in hand"
    def insert(self,value,loc=1):
        if self.head is None:
            print("Dll is not created")
        else:
            node=Node(value)
            if loc==0:
                node.next=self.head
                node.prev=None
                self.head.prev=node
                self.head=node
            elif loc==1:
                node.prev=self.tail
                node.next=None
                self.tail.next=node
                self.tail=node
            else:
                temp=self.head
                count=0
                while count<loc-1:
                    temp=temp.next
                    count+=1
                node.next=temp.next
                node.prev=temp
                temp.next=node
                node.next.prev=node
    def traversal(self):
        print()
        if self.head is None:
            print("No element in the doubly linked list")
        else:
            temp=self.head
            while temp:
                print(temp.value)
                temp=temp.next
    def reverse_traversal(self):
        print()
        if self.head is None:
            print("No element in the doubly linked list")
        else:
            temp=self.tail
            while temp:
                print(temp.value)
                temp=temp.prev
    def delete(self,loc=1):
        if self.head is None:
            print("list is empty")
        else:
            if loc==0:
                self.head=self.head.next
                self.head.prev=None
            elif loc==1:
                self.tail=self.tail.prev
                self.tail.next=None
            else:
                temp=self.head
                count=0
                while count<loc-1:
                    temp=temp.next
                    count+=1
                p=temp.next
                p.next.prev=temp
                temp.next=p.next
                
                
                
            
                
dll=DoublyLinkedList()
dll.create(5)
dll.insert(1,0)
dll.insert(2,0)
dll.insert(3,1)
dll.insert(4,1)
dll.insert(6,2)
dll.insert(8,2)
dll.traversal()
dll.reverse_traversal()
dll.delete(0)
dll.traversal()
dll.delete(2)
dll.reverse_traversal()
dll.delete(3)
dll.reverse_traversal()
print([node.value for node in dll])
