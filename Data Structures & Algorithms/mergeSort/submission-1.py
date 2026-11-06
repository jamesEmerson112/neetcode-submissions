# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        # keep splitting pairs into micro pairs (sub lists)
        # compare them, then combine
        # recursively do the same?
        self.mergeSortHelper(pairs, 0, len(pairs) - 1)

        return pairs


    def mergeSortHelper(self, pairs, left_idx, right_idx):
        if left_idx >= right_idx:
            return

        middle = (left_idx + right_idx) // 2

        self.mergeSortHelper(pairs, left_idx, middle)
        self.mergeSortHelper(pairs, middle + 1, right_idx)

        self.merge(pairs, left_idx, middle, right_idx)
        return

    def merge(self, pairs, left_idx, middle, right_idx):
        temp_left_list = pairs[left_idx:middle+1]
        temp_right_list = pairs[middle+1:right_idx+1]

        i = 0
        j = 0
        k = left_idx

        while i < len(temp_left_list) and j < len(temp_right_list):
            if temp_left_list[i].key <= temp_right_list[j].key:
                pairs[k] = temp_left_list[i]
                i += 1
            else:
                pairs[k] = temp_right_list[j]
                j += 1
            k += 1

        while i < len(temp_left_list):
            pairs[k] = temp_left_list[i]
            i += 1
            k += 1

        while j < len(temp_right_list):
            pairs[k] = temp_right_list[j]
            j += 1
            k += 1
