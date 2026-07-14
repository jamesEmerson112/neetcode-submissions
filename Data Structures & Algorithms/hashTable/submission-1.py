
class HashTable:
    
    def __init__(self, capacity: int):
        self.table = [[] for _ in range(capacity)]
        self.size = 0
        self.capacity = capacity

    def insert(self, key: int, value: int) -> None:
        index = key % self.capacity
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.size += 1

        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = key%self.capacity
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> bool:
        index = key % self.capacity
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.size -= 1
                return True

        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_table = [[] for _ in range(new_capacity)]

        for bucket in self.table:
            for k, v in bucket:
                new_index = k % new_capacity
                new_table[new_index].append((k, v))

        self.table = new_table
        self.capacity = new_capacity
