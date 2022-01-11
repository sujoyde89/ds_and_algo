# sort
# i, j = 0, 0
# if i did not match till n of j then i+q has to start from n+1

def intersection(nums1, nums2):
    nums1.sort()
    nums2.sort()
    
    nums_1_length = len(nums1)
    nums_2_length = len(nums2)
    
    res = []
    i=0
    j=0
    while i<nums_1_length and j<nums_2_length:
        if nums1[i]==nums2[j]:
            res.append(nums1[i])
            i+=1
            j+=1
        elif nums1[i]<nums2[j]:
            i+=1
        elif nums1[i]>nums2[j]:
            j+=1
    return res

nums1, nums2 = [4, 9, 5], [9,4,9,8,4]
# nums1, nums2 = [1, 2, 2, 1], [2, 2]
# nums1,  nums2 = [1, 2], [1, 1]

output = intersection(nums1, nums2)
print (output)
