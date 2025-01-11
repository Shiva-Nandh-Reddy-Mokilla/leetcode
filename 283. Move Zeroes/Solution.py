class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        pos=0
        count=0
        for num in nums:
            if num!=0:
                nums[pos]=num
                pos+=1
                count+=1
        for i in range(count,len(nums)):
            nums[i]=0
            
        
        return nums
          
            

                
