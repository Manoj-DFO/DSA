class Solution(object):
    def maxScore(self, cardPoints, k):
        
        total = sum(cardPoints[:k])
        maximum = total

        for i in range(k):
            total -= cardPoints[k - 1 - i]
            total += cardPoints[len(cardPoints) - 1 - i]
            maximum = max(maximum, total)

        return maximum