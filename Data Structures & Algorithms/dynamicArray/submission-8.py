class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [0] * capacity
        self.capacity  = capacity
        self.length = 0


    def get(self, i: int) -> int:
        return self.array[i]


    # Set n at i-th index
    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize() == self.getCapacity():
            self.resize()
        self.array[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1
        return self.array[self.length]

    def resize(self) -> None:
        self.capacity *= 2
        newArray = [0] * self.capacity
        # deep copy
        for idx in range(len(self.array)):
            newArray[idx] = self.array[idx]

        self.array = newArray


    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.capacity
