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
        temp  = left

        for i in range(left, right):
            if pairs[i].key < pivot.key:
                pairs[temp], pairs[i] = pairs[i], pairs[temp]
                temp += 1

        # put the pivot between the two partitions
        pairs[temp], pairs[right] = pairs[right], pairs[temp]

        self.quickSortHelper(pairs, left, temp - 1)
        self.quickSortHelper(pairs, temp+1, right)