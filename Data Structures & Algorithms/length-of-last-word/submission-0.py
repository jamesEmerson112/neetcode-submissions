class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = 0
        while i < len(s):
            if s[i] == ' ':
                while i < len(s) and s[i] == ' ':
                    i += 1
                if i == len(s):
                    return length
                length = 0
            else:
                length += 1
                i += 1
        return length