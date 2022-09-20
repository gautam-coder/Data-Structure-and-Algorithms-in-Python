from linkedList import LinkedList

def returnkelementtolast(k,ll):
    if ll.head is None:
        return
    else:
        p1=0
        p2=0
        temp=ll.head
        while temp.next:
            temp=temp.next
            p1+=1
        p1-=k
        s=ll.head
        while p2<p1:
            s=s.next
            p2+=1
        s.next=s.next.next
        return ll
ss=LinkedList()
ss.generate(10,0,99)
print(ss)
returnkelementtolast(3,ss)
print(ss)

            
            
