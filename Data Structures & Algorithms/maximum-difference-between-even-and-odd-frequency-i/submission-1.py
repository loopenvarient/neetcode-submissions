class Solution:
    def maxDifference(self, s: str) -> int:
        from collections import Counter
        freq = Counter(s)

        odd = []
        even = []

        for count in freq.values():
            if count % 2 == 0:
                even.append(count)
            else:
                odd.append(count)

        return max(odd) - min(even)
        