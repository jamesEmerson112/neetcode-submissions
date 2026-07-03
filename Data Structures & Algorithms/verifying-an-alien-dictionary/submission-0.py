class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) < 2:
            return False

        order_map = {char: index for index, char in enumerate(order)}

        # iterate the word in words, making sure each word is less than the next word in term of lexicophical order
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            # compare each character in the two words
            for j in range(min(len(word1), len(word2))):
                char1 = word1[j]
                char2 = word2[j]

                if order_map[char1] < order_map[char2]:
                    break
                elif order_map[char1] > order_map[char2]:
                    return False
            else:
                # If we finish the loop without a break, it means the words are identical up to the length of the shorter word
                if len(word1) > len(word2):
                    return False
                
        return True