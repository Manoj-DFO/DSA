class Solution:
    def minBitsFlip(self, start, goal):
        count = 0

        while start > 0 or goal > 0:
            if start % 2 != goal % 2:
                count += 1

            start = start // 2
            goal = goal // 2

        return count