# C Array Abstract Data Type

import ctypes

# Array Abstract Data Type

class Array:
    def __init__(self,*argv):
        self.size = len(argv)
        A =  ctypes.py_object * self.size
        self.array = A()
        for i in argv :
            self.array[argv.index(i)] = i
    def getall(self):
        if self.size == 0 :
            return []
        elif self.size != 0 :
            return [self.array[i] for i in range(self.size)]
    def clear(self):
        self.size = 0
        Empty =  ctypes.py_object * 0
        self.array = Empty()
    def append(self,*argv):
        def NewArray(array,size):
            for i in range(size):
                array[i] = None
            return array
        self.new_size = self.size + len(argv)
        B = ctypes.py_object * self.new_size
        B = B()
        self.Narray = NewArray(B,self.new_size)
        for i in range(self.size):
            self.Narray[i] = self.array[i]
        argvitrat = iter(argv)
        for j in range(self.new_size) :
            if j >= self.size :
                self.Narray[j] = next(argvitrat)

        self.array = self.Narray
        self.size = self.new_size

    def isempty(self):
        if self.size == 0 :
            return True
        elif  self.size != 0:
            return False
    def isexist(self,iteam):
        for i in range(self.size) :
            if iteam == self.array[i] :
                RESULT = True
        try : 
            return RESULT
        except UnboundLocalError:
            return False
    def index(self,iteam):
        RESULT = self.isexist(iteam)
        if RESULT == True:
            for i in range(self.size):
                if iteam == self.array[i]:
                    return i
                else:
                    pass
        else:
            NotFoundIteam = f'{iteam} Not Exist'
            return NotFoundIteam
    def insert(self,index):
        pass
if __name__ == "__main__" :
    # from ArrayADT import Array
    A = Array(1,2,3,4,5)
    print(A.getall())
    A.clear()
    print(A.getall())
    print(A.isexist(10))
    print(A.index(1))
    

