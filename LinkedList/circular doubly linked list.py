class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
class CircularDoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
            if node==self.tail.next:
                break

    def create(self,value):
        node=Node(value)
        self.head=node
        self.tail=node
        node.prev=node
        node.next=node
    def insert(self,value,loc=1):
        if self.head is None:
            print("Circular linked list is not exist")
        else:
            node=Node(value)
            if loc==0:
                node.next=self.head
                node.prev=self.tail
                self.head.prev=node
                self.head=node
                self.tail.next=node
            elif loc==1:
                self.tail.next=node
                node.next=self.head
                node.prev=self.tail
                self.head.prev=node
                self.tail=node
            else:
                temp=self.head
                count=0
                while count<loc-1:
                    temp=temp.next
                    count+=1
                node.prev=temp
                node.next=temp.next
                temp.next=node
                node.next.prev=node
    def traversal(self):
        temp=self.head
        while temp:
            print(temp.value)
            if temp ==self.tail:
                break
            temp=temp.next
    def reverse_traversal(self):
        temp=self.tail
        while temp:
            print(temp.value)
            if temp==self.head:
                break
            temp=temp.prev
        #self.traversal()
    def search(self,value):
        temp=self.head
        while temp:
            if temp.value == value:
                print(temp.value,"is found")
                break
            if temp==self.tail:
                print("value not found")
                break
            temp=temp.next
    def delete(self,loc):
        if self.head is not None:
            if loc==0:
                if self.head==self.tail:
                    self.head.prev=None
                    self.head.next=None
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
                    self.tail.next=self.head
                    self.head.prev=self.tail
            elif loc==1:
                if self.head==self.tail:
                    self.head.prev=None
                    self.head.next=None
                    self.head=None
                    self.tail=None
                else:
                    self.tail=self.tail.prev
                    self.tail.next=self.head
                    self.head.prev=self.tail
            else:
                temp=self.head
                count=0
                while count<loc:
                    temp=temp.next
                    count+=1
                temp.next=temp.next.next
                temp.next.prev=temp                
        else:
            print("list is empty")
    def delete_entire(self):
        if self.head is None:
            print("No element is present in the list")
        else:
            self.tail.next=None
            temp=self.head
            while temp:
                temp.prev=None
                temp=temp.next
            self.head=None
            self.tail=None
                
                

                
                
        
cdll=CircularDoublyLinkedList()
cdll.create(2)
cdll.insert(3,0)
cdll.insert(4,1)
cdll.insert(5,1)
cdll.insert(6,2)
cdll.insert(7,2)
#cdll.traversal()
cdll.reverse_traversal()
cdll.search(2)
cdll.delete(2)
cdll.reverse_traversal()
print()
cdll.delete_entire()
print([i.value for i in cdll])
