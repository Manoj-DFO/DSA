class Solution(object):
    def findMin(self, nums):
        
        high = len(nums) - 1
        low = 0

        while low < high:

            mid = (low + high) // 2

            if nums[low] == nums[high] == nums[mid]:
                low += 1
                high -= 1

            elif nums[mid] > nums[high]:

                low = mid + 1

            else:

                high = mid

        return nums[low]