# https://leetcode.com/problems/two-sum/
# compliment map with index
# search in compliment map

def twoSum(nums, target):

    length = len(nums)
    compliment_map = {}

    for i in range(length):
        num = nums[i]
        compliment = target - num
        if num in compliment_map:
            return [compliment_map[num], i]
        else:
            compliment_map[compliment] = i

nums = [3,2,4]
target = 6
output = twoSum(nums, target)
print (output)
