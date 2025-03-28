class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numbers={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in numbers:
                return [numbers[diff],i]
            numbers[n]=i
        