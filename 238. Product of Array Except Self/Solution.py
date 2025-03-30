class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        prefix=1
        suffix=1
        new=[1]*len(nums)
        for i in range(len(nums)):
            new[i]=prefix
            prefix=nums[i]*prefix
            
        for i in range(len(nums)-1,-1,-1):
            new[i]=suffix*new[i]
            suffix=nums[i]*suffix
        return new

         
           



            
       
            