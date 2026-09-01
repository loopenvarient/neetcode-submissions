class Solution:
    def countSeniors(self, details: List[str]) -> int:
        #details ia a string which can have many passengers,
        #length of each passemger is 15
        #1-10 is phone, 11 is G, 12,13 combines age, 14,15 combines to give seat
        count = 0
        for x in details:
            x = x.strip()

            if int(x[11:13]) > 60:  # 11:13 means 12 and 13
                count += 1
        return count
