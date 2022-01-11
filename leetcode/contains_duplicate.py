# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/578/
# store all seen elements in set

def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)
    return False

# nums = [1,2,3,1]
nums = [1,2,3,4]
output = contains_duplicate(nums)
print (output)