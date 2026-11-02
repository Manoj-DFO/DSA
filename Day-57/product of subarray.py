class Solution(object):
    def maxProduct(self, nums):

        maxx = minn = result = nums[0]
        
        for i in range(1, len(nums)):

            if nums[i] < 0:
                maxx, minn = minn, maxx

            maxx = max(nums[i], nums[i]*maxx)
            minn = min(nums[i], nums[i]*minn)

            result = max(result, maxx)

        return result