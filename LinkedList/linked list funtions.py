from random import randint
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        self.prev=None
    def __str__(self):
        return str(self.value)
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        temp=self.head
        while temp:
            yield temp
            temp=temp.next
    def __str__(self):
        v=[str(i.value) for i in self]
        return ' -> '.join(v)
    def add(self,value):
        if self.head is None:
            node=Node(value)
            self.head=node
            self.tail=node
        else:
            self.tail.next=Node(value)
            self.tail=self.tail.next
            return self.tail
    def generate(self,n,mi,ma):
        self.head=None
        self.tail=None
        for i in range(n):
            self.add(randint(mi,ma))
        return self
ll=LinkedList()
ll.generate(10,0,30)
print(ll)
