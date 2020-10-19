import gc
class DoublyLinked :
    def __init__(self):
        self.startnode = None
    def add(self,*argv):          # add to start
      for data in argv : 
        NewNode = Node(data)            # creat new node using class Node
        NewNode.next = self.startnode   # make the NewNode as the head by setting the .next to the current startnode
        if self.startnode is not None:  # check if List not empty
            self.startnode.prev = NewNode   # if not empty set the current startnode.prev to the NewNode
        self.startnode = NewNode        # startnode will be the current Node

    def travers(self):           # display all data in list
        if self.startnode == None :     # check if List not empty
            raise Exception('Linked List Empty !')  
        else:                           
            n = self.startnode          
            while n != None:
                print(n.data, end=',')
                n = n.next
                if n == None :
                    print(None)
    def remove(self,iteam):
        if self.isexist(iteam) == True :
            if self.startnode.data == iteam :
                self.startnode = self.startnode.next
            else : 
                NodeObj = self.isexist(iteam,ReturnJustObject=True)
                if NodeObj.next == None :
                    NodeObj.prev.next = None 
                else : 
                    NodeObj.prev.next = NodeObj.next
                    NodeObj.next.prev = NodeObj.prev
        else : 
            print(f'{iteam} not found')
        gc.collect()
    def isexist(self,iteam,ReturnJustObject=False):
        sN = self.startnode  # startNode
        while sN != None:
            if sN.data == iteam :
                RESULT = True
                NodeObject =  sN
                break
            else :
                RESULT = False
            sN = sN.next
        if ReturnJustObject == True :
            return NodeObject
        elif ReturnJustObject == False :
            return RESULT
    def getlast(self):
        N = self.startnode
        while N != None:
            if N.next == None :
                Last = N
            N = N.next
        return Last
    def append(self,*argv):
        last = self.getlast()
        for data in argv :
            NewLastNode = Node(data)
            last.next = NewLastNode
            NewLastNode.prev = last
            last = NewLastNode            
    def insert(self, insertin=None,*argv):
        if insertin != None :
            if self.isexist(insertin) == True:

                for data in argv:
                    BeforNewNode = self.isexist(insertin, ReturnJustObject=True)
                    AfterNewNode = BeforNewNode.next
                    NewinsertNode = Node(data)
                    NewinsertNode.prev = BeforNewNode
                    NewinsertNode.next = AfterNewNode
                    BeforNewNode.next = NewinsertNode
                    AfterNewNode.prev = NewinsertNode
                    BeforNewNode = NewinsertNode
                    gc.collect()
            else :
                print(f'{insertin} not found')
        else:
            print('we can\'t find where to insert your new items')
    def replace(self,value,target):
        if self.isexist(target) == True:
            target = self.isexist(target,ReturnJustObject=True)
            target.data = value
        else :
            print('Target Not Found')


class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


DLK = DoublyLinked()
DLK.add(1,2,3,5,6,8,9,7)
DLK.travers()
DLK.insert(5,'Hamza','Hafsa','Hajar')
DLK.travers()
DLK.insert('Hajar',123)
DLK.travers()
DLK.replace('LALALALALA','Hajar')
DLK.travers()
