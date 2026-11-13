class Solution(object):
    def minBitFlips(self, start, goal):
        count = 0

        while start > 0 or goal > 0:
            if start % 2 != goal % 2:
                count += 1

            start = start // 2
            goal = goal // 2

        return count

class Solution(object):
    def minBitFlips(self, start, goal):
        ans = start ^ goal
        ansstr=str(bin(ans))
        count=0
        for i in ansstr:
            if i == "1":
                count=count+1
        return count