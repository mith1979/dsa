class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.len = 0
        self.dyn_arr = [0] * self.capacity
        
    def get(self, i: int) -> int:
        return self.dyn_arr[i]

    def set(self, i: int, n: int) -> None:
        self.dyn_arr[i] = n
        self.print_arr()

    # pushback(int n) will push the element n to the end of the array.
    def pushback(self, n: int) -> None:
        #check if the len(dyn_arr) == capacity
        if self.len == self.capacity:
            self.resize()
        self.dyn_arr[self.len]=n
        self.len +=1

        self.print_arr()
    # popback() will pop and return the element at the end of the array. Assume that the array is non-empty.
    def popback(self) -> int:
        #self.len -=1
       
        if self.len >0:
            last_ele = self.dyn_arr[self.len-1]
            self.dyn_arr[self.len-1] = 0
            print(f"poping back ele : {last_ele}")
            self.len -=1
            return last_ele
        
    # resize() will double the capacity of the array.
    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity
        for i in range(self.len):
            new_arr[i] = self.dyn_arr[i]
        self.dyn_arr = new_arr
        self.print_arr()

    def getSize(self) -> int:
        print(f"Size of the ARRAY:{len(self.dyn_arr)}")
        return self.len
    
    def getCapacity(self) -> int:
        print(f"Capacity of the ARRAY:{self.capacity}")
        return self.capacity
    
    def print_arr(self):
        print(f"FINAL ARRAY{self.dyn_arr}")


d = DynamicArray(2)
d.pushback(1)
d.pushback(2)
d.getSize()
d.getCapacity()
d.pushback(3)
d.getSize()
d.getCapacity()
d.pushback(4)
d.getSize()
d.getCapacity()
d.popback()
d.getSize()
d.getCapacity()
d.pushback(5)
d.getSize()
d.getCapacity()
d.pushback(6)
d.getSize()
d.getCapacity()
d.print_arr()




