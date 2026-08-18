class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n= s.split()[-1]
        return (len(n))
        