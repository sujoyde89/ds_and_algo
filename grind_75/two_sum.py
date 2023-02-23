class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            n1 = nums[i]
            n2 = target-nums[i]
            if n2 in nums_dict:
                return [nums_dict[n2], i]
            nums_dict[n1]=i
