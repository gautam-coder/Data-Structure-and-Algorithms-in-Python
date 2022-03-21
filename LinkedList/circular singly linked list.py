class Node:
    def __init__(self,value=None):
        self.value=value
        self.node=None
class circularSinglyLinkedList:
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
            
    def createcsll(self,nodevalue):
        node=Node(nodevalue)
        node.next=node
        self.head=node
        self.tail=node
    def insert(self,value,location=0):
        if self.head is None:
            return "the head refernce is none"
        else:
            newNode=Node(value)
            if location==0:
                newNode.next=self.head
                self.head=newNode
                self.tail.next=newNode
            elif location==1:
                newNode.next=self.tail.next
                self.tail.next=newNode
                self.tail=newNode
            else:
                count=0
                temp=self.head
                while count<location-1:
                    temp=temp.next
                    count+=1
                nextNode=temp.next
                temp.next=newNode
                newNode.next=nextNode
    def traversal(self):
        if self.head is None:
            print("No element is present")
        else:
            temp=self.head
            while temp:
                print(temp.value)
                temp=temp.next
                if temp==self.tail.next:
                    break
    def search(self,valu):
        if self.head is None:
            print("No element is present")
        else:
            temp=self.head
            while temp:
                if temp.value == valu:
                    print(valu,temp.next)
                    break
                temp=temp.next
                if temp==self.tail.next:
                    print("value not present")
                    break
    def delete(self,location):
        if self.head is None:
            print("there is not any node")
        else:
            if location==0:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                    self.head.next=None
                else:
                    self.head=self.head.next
                    self.tail.next=self.head
            elif location==1:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                    self.head.next=None
                else:
                    node=self.head
                    while node is not None:
                        if node.next==self.tail:
                            break
                        node=node.next
                    node.next=self.head
                    self.tail=node
            else:
                node=self.head
                index=0
                while index<location-1:
                    node=node.next
                    index+=1
                nextNode=node.next
                node.next=nextNode.next
                
                
                
                


                
cc=circularSinglyLinkedList()
cc.createcsll(1)
cc.insert(2,0)
cc.insert(3,0)
cc.insert(4,2)
cc.traversal()
cc.search(4)
cc.delete(2)
print([node.value for node in cc])
            
