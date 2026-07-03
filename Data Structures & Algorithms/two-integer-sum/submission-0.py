class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # basically we iterate the loop, if target - the current number = remainder, whereas remainder is in the nums, return those two numbers
        nums_map = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in nums_map:
                return [nums_map[remainder], i]
            nums_map[nums[i]] = i

        return []