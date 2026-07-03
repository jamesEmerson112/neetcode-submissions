class Solution:
    def isValid(self, s: str) -> bool:
        # basically we want to keep track f these: '(', ')', '{', '}', '[' and ']'
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []

        # brute force, we are going to use stack with append and pop to keep track of order
        for char in s:
            if char in mapping:
                top = stack.pop() if stack else '#'
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)

        return True if not stack else False