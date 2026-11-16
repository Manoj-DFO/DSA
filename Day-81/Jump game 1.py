nums = [2, 3, 1, 1, 4]

def reach(nums):

    maximum = 0

    for i in range(len(nums)):

        if i > maximum:
            return False
        
        maximum = max(maximum, i + nums[i])
    return True

print(reach(nums))