# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/727/#

def removeDuplicates(nums):
    length = len(nums)
    i = 1
    while i<length:
        if nums[i] == nums[i-1]:
            del nums[i]
            length -= 1
        else:
            i+=1
    print (nums)
    return i

nums = [0,0,1,1,1,2,2,3,3,4]
i = removeDuplicates(nums)
print (i)