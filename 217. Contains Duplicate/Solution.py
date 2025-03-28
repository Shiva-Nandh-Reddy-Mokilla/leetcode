class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        i=1
        while i<len(nums):
            if nums[i]==nums[i-1]:
                return True
            i+=1
        return False