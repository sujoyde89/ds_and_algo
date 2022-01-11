# https://leetcode.com/problems/3sum/
# sort
# i, l, r
# if sum < 0 l+1
# if sum > 0 r-1
# if sum = 0 l+1, r-1

def threeSum(nums):
    res = []
    nums.sort()
    length = len(nums)

    for i in range(length-2):
            
            if i>0 and nums[i]==nums[i-1]: # process has been done for i
                continue
                
            l = i+1
            r = length-1

            while l<r:            
                total = nums[i] + nums[l] + nums[r]
                
                if total<0:
                    l = l+1
                elif total>0:
                    r = r-1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l<r and nums[l]==nums[l+1]: # remove duplicate triplet
                        l=l+1
                    while l<r and nums[r]==nums[r-1]: # remove duplicate triplet
                        r=r-1
                    l = l+1
                    r = r-1
    return res

nums = [-1,0,1,2,-1,-4]
res = threeSum(nums)
print (res)
