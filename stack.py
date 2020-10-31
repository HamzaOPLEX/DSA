# push :    add in Head     =>  [1,2,3,6].push(5) => [5,1,2,3,6]
# peek :    return Top iteam       => [1,2,3,6].peek() => 6
# pop  :    remove and return Head iteam [1,2,3,6].pop() => 1

# let implement stack using linked list

class stack :
    def __init__(self):
        self.head = None
        self.size = 0
    def __str__(self):
        N = self.head
        out = ''
        while N != None:
            out += f'{N.data} ->'
            N = N.next
        return out[:-3]
    def isEmpty(self) :
        if self.size == 0 :
            return True
        elif self.size != 0 :
            return False
    def getSize(self):
        return self.size
    def push(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size += 1
    def peek(self): # last node in linked list
        if self.isEmpty() == True:
            raise Exception('Cannot pop from an empty stack')
        else:
            N = self.head 
            while N != None:
                if N.next == None:
                    return N.data
                    break
                N = N.next
    def pop(self):
        if self.isEmpty() == True :
            raise Exception ('Cannot pop from an empty stack')
        else :
            removed = self.head.data
            self.head = self.head.next
            self.size -= 1
            return removed
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None


if __name__ == '__main__' :
    s = stack()
    s.push(10)
    s.push(15)
    s.push(16)
    s.push(17)
    s.push(367)
    s.push(7)
    s.push(175)
    s.push(1755)
    print(s)

    print('peek :',s.peek())
    while s.isEmpty() != True :
        print('pop : ',s.pop())

