class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        d = {}
        for letter in sentence:
            if letter in d:
                d[letter] += 1
            else:
                d[letter] = 1
        return len(d) == 26
        
