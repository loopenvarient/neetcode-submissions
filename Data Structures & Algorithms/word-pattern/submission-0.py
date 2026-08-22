class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        mapping = {}

        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]

            if char in mapping:
                if mapping[char] != word:
                    return False
            else:
                mapping[char] = word

        return len(mapping) == len(set(words))