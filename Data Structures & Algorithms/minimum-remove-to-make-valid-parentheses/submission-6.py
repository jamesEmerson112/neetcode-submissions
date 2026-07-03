class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        openCount = closeCount = 0

        for c in s:
            closeCount += c == ')'

        res = []
        for c in s:
            if c == '(':
                if openCount == closeCount:
                    continue
                openCount += 1
            elif c == ')':
                closeCount -= 1
                if openCount == 0:
                    continue
                openCount -= 1
            res.append(c)

        return ''.join(res)