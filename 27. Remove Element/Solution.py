class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n=0
        while n<len(nums):
            if nums[n]==val:
                nums.pop(n)
                n=n-1
            n+=1
        return len(nums)