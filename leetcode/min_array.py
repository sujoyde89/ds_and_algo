def get_minimum(nums):
    length = len(nums)
    i = 1
    minimum = nums[0]
    while i<length:
        if nums[i]<minimum:
            minimum = nums[i]
        i+=1
    print (minimum)
    return minimum

nums = [2, 3, 4, 8, 4, 3, 1]
get_minimum(nums)