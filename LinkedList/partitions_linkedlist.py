from linkedList import LinkedList

def partition(ll,x):
    cur=ll.head
    ll.tail=ll.head

    while cur:
        nextnode=cur.next
        cur.next=None
        if cur.value<x:
            cur.next=ll.head
            ll.head=cur
        else:
            ll.tail.next=cur
            ll.tail=cur
        cur=nextnode
    if ll.tail.next is not None:
        ll.tail.next=None

cu=LinkedList()
cu.generate(15,0,99)
print(cu)
partition(cu,50)
print(cu)
