class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n=len(nums)/2
        count=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                count+=1
                
            else:
                count=0
            if count>n:
                return nums[i]
        return nums[len(nums)//2]
            
            

