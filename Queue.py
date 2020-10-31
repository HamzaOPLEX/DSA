# enqueue() : add new item to Queue
# dequeue() : remove and return item from Last Queue
# peek()    : return the head 
# isEmpty() : check if Queue is Empty
# getSize() : get size of the Queue


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def __str__(self):
        if self.size == 0 : 
            return 'Queue empty'
        else : 
            N = self.head
            out = ''
            while N != None:
                out += f'{N.data} ->'
                N = N.next
            return out[:-3]

    def isEmpty(self):
        if self.size == 0:
            return True
        elif self.size != 0:
            return False
    def getSize(self):
        return self.size
    def enqueue(self,data):
        node = Node(data)
        self.size += 1
        if self.head == None: # if LinkedList empty head = NewNode , Tail = NewNode
            self.head = node  
            self.tail = node
        else:                # if LinkedList Not empty
            self.tail.next = node   # point the tail to the new node (FIFO)
            self.tail = node        # put the newnode as the tail of the LinkList
    def dequeue(self):
        if self.isEmpty() == True:
            raise Exception('Cannot dequeue from an empty Queue')
        else:
            removed = self.head.data
            self.head = self.head.next
            self.size -= 1
            return removed

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(10)
    queue.enqueue(100)
    queue.enqueue(1000)
    # print(queue)
    while queue.getSize() != 0:
        print('dequeue :',queue.dequeue())
    print(queue)
