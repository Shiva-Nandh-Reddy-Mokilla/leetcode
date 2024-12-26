class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        prefix=1
        suffix=1
        result=[1]*n
        for i in range(n):
            result[i]=prefix
            prefix=prefix*nums[i]

        for i in range(n-1,-1,-1):
            result[i]*=suffix
            suffix=suffix*nums[i]
        return result
        



            
       
            