class Solution(object):
    def candy(self, ratings):
        
        n = len(ratings)
        up = down = peak = 0
        candies = 1

        for i in range(1,n):

            if ratings[i] > ratings[i - 1]:
                up += 1
                down = 0
                peak = up
                candies += 1 + up

            elif ratings[i] < ratings[i - 1]:
                up = 0
                down += 1
                candies += 1 + down
                if peak >= down:
                    candies -= 1

            else:
                up = 0
                down = 0
                peak = 0
                candies += 1

        return candies