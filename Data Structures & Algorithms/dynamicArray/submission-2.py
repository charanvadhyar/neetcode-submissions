import ctypes
class DynamicArray:

    
    
    def _make_buffer(self, capacity):
         return (capacity * ctypes.py_object)()

    def __init__(self, capacity: int):
        self.length = 0
        self.capacity = capacity
        self.data = self._make_buffer(self.capacity)


    def get(self, i: int) -> int:
        return self.data[i]
        


    def set(self, i: int, n: int) -> None:
        self.data[i] = n


    def pushback(self, n: int) -> None:

        if self.length == self.capacity:
            self.resize()
        self.data[self.length] = n;
        self.length = self.length+1


    def popback(self) -> int:
        self.length = self.length-1
        return self.data[self.length]
 

    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_data = self._make_buffer(new_capacity)
        for i in range(self.length):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity


    def getSize(self) -> int:

        return self.length
        
    
    def getCapacity(self) -> int:
        return self.capacity