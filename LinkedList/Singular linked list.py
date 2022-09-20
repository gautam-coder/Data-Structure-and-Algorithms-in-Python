class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        
class singlyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
    def insert(self,value,location=1):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            if location==0:
                newNode.next=self.head
                self.head=newNode
            elif location==1:
                newNode.next=None
                self.tail.next=newNode
                self.tail=newNode
            else:
                temp=self.head
                index=0
                while index<location-1:
                    temp=temp.next
                    index+=1
                nextNode=temp.next
                temp.next=newNode
                newNode.next=nextNode
    def traversal(self):
        node=self.head
        if self.head is None:
            print("No element")
        else:
            while node:
                print(node.value)
                node=node.next
    def search(self,value):
        node=self.head
        if node is None:
            print("No element")
        else:
            while node:
                if node.value==value:
                    print("get it")
                    break
                node=node.next
    def delete(self,location):
        if self.head is None:
            print("doesn't exist")
        else:
            if location==0:
                if self.head ==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
            elif location ==1:
                if self.head ==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    node=self.head
                    index=0
                    while node is not None:
                        if node.next==self.tail:
                            break
                        node=node.next
                        index+=1
                    node.next=None
                    self.tail=node
            else:
                node=self.head
                index=0
                while index<location-1:
                    node=node.next
                    index+=1
                new=node.next
                node.next=new.next
    def deleteAll(self):
        if self.head is None:
            print("doesn't exist")
        else:
            self.head=None
            self.tail=None
        
sll=singlyLinkedList()
#sll.insert(1,1)
for i in range(10):
    sll.insert(i)
sll.insert(10,2)
sll.traversal()
sll.search(20)
sll.delete(1)
#sll.deleteAll()
print([node.value for node in sll])
        
