class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # finidng largest lucky number based on frequency
        hashmap={}
        for num in arr:
            if num in hashmap:
                hashmap[num] +=1
            else:
                hashmap[num] = 1

        max_lucky = -1
        for num, freq in hashmap.items():
            if num == freq:
                max_lucky = max(max_lucky, num)
        return max_lucky