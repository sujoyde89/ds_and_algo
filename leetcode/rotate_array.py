# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/646/

def rotate(nums, k):
    for i in range(1, k+1):
        nums = [nums[-1]] + nums
        del nums[-1]
    print (nums)

nums = [1,2,3,4,5,6,7]
rotate(nums, 3)