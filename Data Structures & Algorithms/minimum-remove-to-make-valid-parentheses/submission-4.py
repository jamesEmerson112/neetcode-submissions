class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # list of indices to remove
        indices_to_remove = []

        # iterate through the string to count the leading right parentheses
        leading_right_parentheses = 0
        for i in range(len(s)):
            if s[i] == ')':
                leading_right_parentheses += 1
                indices_to_remove.append(i)
            elif s[i] == '(':
                # exit the loop
                break

        ending_left_parentheses = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                ending_left_parentheses += 1
                indices_to_remove.append(i)
            elif s[i] == ')':
                # exit the loop
                break

        # sort the indices to remove
        indices_to_remove.sort()
        clean_str = ''
        # given the array of indices to remove, remove the characters at those indices from the string s
        result = []
        remove_set = set(indices_to_remove)
        for i in range(len(s)):
            if i not in remove_set:
                result.append(s[i])
                clean_str = ''.join(result)

        # with the clean string, keep count of left and right parentheses
        # if right parentheses exceed left parentheses, remove the right parentheses
        left_count = 0
        right_count = 0

        print(left_count, right_count)


        result = []
        # a character or more must be between a pair of parentheses as well
        for i in range(len(clean_str)):
            print(clean_str[i])
            if clean_str[i] == '(':
                left_count += 1
                is_left_parenthesis = True
            elif clean_str[i] == ')':
                right_count += 1
                if right_count > left_count:
                    right_count -= 1
                    continue
            result.append(clean_str[i])

        # if there are more left parentheses than right parentheses, remove the excess left parentheses from the end
        # in reverse order
        if left_count > right_count:
            excess_left = left_count - right_count
            for i in range(len(result) - 1, -1, -1):
                if excess_left == 0:
                    break
                if result[i] == '(':
                    result.pop(i)
                    excess_left -= 1

        print(left_count, right_count)

        return ''.join(result)