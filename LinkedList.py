# 1 - Creat LinkedList class With the StartNode(Head) is Null
# 2 - Creat Node Class with The Data,Next

class  LinkedList :
    def __init__(self) :
        self.startnode = None
    def insertHead(self,*argv): # insert at start
        for data in argv : 
            New_Node = Node(data)   # Creat New Node using Node(data) and save it in New_Node Var
            New_Node.next = self.startnode  # Change New_Node.next from Null to the current value of self.startnode
            self.startnode = New_Node   # After that the Startnode will be the New_Node
    def insert(self,beforiteam,*argv) : # insert on random place
        if self.isexist(beforiteam) == True :
            BeforeIteamObject = self.isexist(beforiteam,ReturnJustObject=True)
            for data in argv :
                NewObjectNode = Node(data)
                NewObjectNode.next = BeforeIteamObject.next
                BeforeIteamObject.next = NewObjectNode
                BeforeIteamObject = NewObjectNode
        else:
            print('Befor Iteam not Found !')

    def insertTail(self,*argv): #  insert at the end
        if self.startnode != None:  # Check if LinkedList is empty
            N = self.startnode      #
            while N != None:        # Search for the Last iteam in The current LinkedList
                if N.next == None :
                    Last = N
                N = N.next
            for i in argv :             # Insert argv at end 
                NewLastNode = Node(i)   # crear new node for each iteam in argv
                Last.next = NewLastNode # Make The old Last node point to the new Last Node by chaning His .next
                Last = NewLastNode      # Make The NewLastNode as Last Node
        else:
            print('list is empty use insertHead')
    def travers(self): # print all iteam in Linked List
        # Check if LinkedList is Empty
        if self.startnode == None:
            print('LinkedList is empty !')
        else :
            n = self.startnode
            while n != None:
                print(n.data,end='->')
                n = n.next
                if n == None :
                    print(None,'\n')
    def travers_asList(self):
        # Check if LinkedList is Empty
        if self.startnode == None:
            print('LinkedList is empty !')
        else :
            n = self.startnode
            OUTPUT = []
            while n != None:
                OUTPUT.append(n.data)
                n = n.next
            return OUTPUT
    def remove(self,data): # Still not complted
        if self.isexist(data) == True :
            if data == self.startnode.data :
                self.startnode = self.startnode.next
            else :
                N = self.startnode
                while N != None :
                    try : 
                        if str(N.next.data) == data :
                            BeforTargetIteam = N
                        elif str(N.data) == data :
                            TargetIteam = N
                            AfterTargetIteam = N.next
                        N = N.next
                    except Exception as err :
                        break
                BeforTargetIteam.next = AfterTargetIteam
                TargetIteam.data = None
                TargetIteam.next = None
        else :
            print('iteam not found !')
    def isexist(self,iteam,ReturnJustObject=False) :
        Nd = self.startnode
        while Nd != None :
            if Nd.data == iteam :
                RESULT =  True
                NodeObject = Nd
                break
            elif Nd.data != iteam :
                RESULT = False
            Nd = Nd.next
        if ReturnJustObject == True :
            return NodeObject
        elif ReturnJustObject == False :
            return RESULT

            

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

if __name__ == '__main__' :

    Linked = LinkedList()
    Linked.insertHead("Hamza",'Data','DOTO','1515')
    Linked.insertTail(1,2,3,6)
    Linked.travers()
    Linked.remove('DOTO')
    Linked.travers()
    # print(Linked.isexist('Hamza'))
    print(Linked.travers_asList())
    Linked.insert("Hamza",'OPLEX','Laylay',1,2,3)
    Linked.travers()
