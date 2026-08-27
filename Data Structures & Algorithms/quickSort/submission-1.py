# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        # since it needs a pitvot, I should create a helper as well 
        self.quickSortHelper(pairs, 0, len(pairs)-1)
        return pairs

    def quickSortHelper(self, pairs, left, right):
        if left >= right:
            return

        # the right is always the pivot
        pivot = pairs[right]
        store = left

        for i in range(left, right):
            if pairs[i].key < pivot.key:
                pairs[store], pairs[i] = pairs[i], pairs[store]
                store += 1

        # put the pivot between the two partitions
        pairs[store], pairs[right] = pairs[right], pairs[store]

        self.quickSortHelper(pairs, left, store - 1)
        self.quickSortHelper(pairs, store+1, right)