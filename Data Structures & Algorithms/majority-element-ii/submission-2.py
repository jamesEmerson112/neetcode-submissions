class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        color1 = color2 = -1
        count1 = count2 = 0

        for color in nums:
            if color == color1:
                count1 += 1
            elif color == color2:
                count2 += 1
            elif count1 == 0:
                count1 = 1
                color1 = color
            elif count2 == 0:
                count2 = 1
                color2 = color
            else:
                count1 -= 1
                count2 -= 1

        count1 = count2 = 0

        for color in nums:
            if color == color1:
                count1 += 1
            elif color == color2:
                count2 += 1

        res = []
        if count1 > n // 3:
            res.append(color1)
        if count2 > n // 3:
            res.append(color2)

        return res