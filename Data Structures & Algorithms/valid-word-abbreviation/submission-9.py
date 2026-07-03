class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0

        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isalpha() or abbr[j] == '0':
                return False
            else:
                num_str = ''
                while j < len(abbr) and abbr[j].isdigit():
                    num_str += abbr[j]
                    j += 1
                i += int(num_str)
        
        return i == len(word) and j == len(abbr)