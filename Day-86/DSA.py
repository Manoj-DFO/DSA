class Solution(object):
    def longestOnes(self, nums, k):
        
        maximum = left = zeros = 0

        for i in range(len(nums)):

            if nums[i] == 0:
                zeros += 1

            while zeros > k:

                if nums[left] == 0:
                    zeros -= 1

                left += 1

            maximum = max(maximum, i - left + 1)

        return maximum