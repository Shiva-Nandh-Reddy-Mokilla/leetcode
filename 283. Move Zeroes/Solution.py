class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        new = [num for num in nums if num != 0]  
       
        for i in range(len(new)):
            nums[i] = new[i]
        for i in range(len(new), len(nums)):
            nums[i] = 0
        
        return new  
            

                
