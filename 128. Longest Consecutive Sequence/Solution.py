class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        i=1
        count=0
        countmax=0
        for i in range(len(nums)):
            if nums[i] == nums[i - 1]:  
                continue
            elif nums[i]==nums[i-1]+1:
                count+=1
                countmax=max(count,countmax)
            else:
                count=0
        return countmax+1
        
        