class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count=0
        i=1
        while i<len(nums):
            if nums[i]==nums[i-1]:
                count+=1
                if count>1:
                    nums.pop(i)
                else:
                    i+=1
                    
                
            else:
                count=0
                i+=1
        
        
       
        