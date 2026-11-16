class Solution(object):
    def jump(self, nums):
        
        maximum = current_end = steps = 0

        for i in range(len(nums) - 1):

            maximum = max(maximum, i + nums[i])

            if i == current_end:
                steps += 1
                current_end = maximum

        return steps