class Solution:
    def isPalindrome(self, s: str) -> bool:
        # O(n) time | O(1) space
        # two pointers approach, if seeing non alphabet characters, skip them
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            print(s[left], s[right] )
            temp1 = s[left].lower()
            temp2 = s[right].lower()
            if temp1 != temp2:
                return False
            left += 1
            right -= 1

        return True