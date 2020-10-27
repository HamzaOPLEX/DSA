# Simple Circular Linked List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLL:
    def __init__(self):
        self.startnode = None
        self.endnode = None
    def travers(self):
        print('\n')
        N = self.startnode 
        while N:
            print(N.data,end=' ')
            N = N.next  
            if N == self.startnode:
                break
    def add(self,*argv):
        for data in argv :
            NewNode = Node(data) # Creat NewNode
            NewNode.next = self.startnode # Point NewNode to The start Node
            if self.startnode == None:    # if List not empty The NewNode will Point to his self 
                NewNode.next = NewNode
                self.startnode = NewNode
                self.endnode = NewNode
            elif self.startnode != self.endnode and self.startnode != None :  # if List not empty and startnode don't point to his self
                NewNode.next = self.startnode
                self.endnode.next = NewNode
            self.startnode = NewNode

if __name__ == '__main__':
    run  = CircularLL()
    run.add(1,2,3,6,8,9)
    run.travers()
