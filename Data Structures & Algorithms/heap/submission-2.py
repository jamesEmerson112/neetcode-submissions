class MinHeap:
    
    def __init__(self):
        self.priority_queue = []

    def push(self, val: int) -> None:
        self.priority_queue.append(val)
        i = len(self.priority_queue) - 1

        while i > 0:
            parent = (i - 1) // 2
            if self.priority_queue[parent] <= self.priority_queue[i]:
                break

            self.priority_queue[parent], self.priority_queue[i] = (
                self.priority_queue[i],
                self.priority_queue[parent],
            )

            i = parent

    def isEmpty(self) -> int:
        return len(self.priority_queue) == 0

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        # min heap always has the root (0th index) to be the minimum item

        root = self.priority_queue[0]

        last = self.priority_queue.pop()

        if self.priority_queue:
            self.priority_queue[0] = last
            self.bubble_down(0)

        return root

    def bubble_down(self, i):
        n = len(self.priority_queue)

        while True:
            left = 2 * i + 1
            right = 2 * i + 2

            smallest = i

            if left < n and self.priority_queue[left] < self.priority_queue[smallest]:
                smallest = left

            if right < n and self.priority_queue[right] < self.priority_queue[smallest]:
                smallest = right

            if smallest == i:
                break

            self.priority_queue[i], self.priority_queue[smallest] = (
                self.priority_queue[smallest],
                self.priority_queue[i]
            )

            i = smallest

    def top(self) -> int:
        return self.priority_queue[0] if self.priority_queue else -1

    def heapify(self, nums: List[int]) -> None:
        self.priority_queue = nums[:]
        n = len(self.priority_queue)

        for i in range(n//2-1, -1, -1):
            self.bubble_down(i)
        