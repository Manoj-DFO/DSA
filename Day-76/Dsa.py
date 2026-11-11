class Solution(object):
    def longestConsecutive(self, nums):
        
        result = 0
        num_set = set(nums)
        for n in num_set:

            if n-1 not in num_set:
                count = 1

                while n+1 in num_set:

                    count += 1
                    n += 1
            
                result = max(result, count)

        return result