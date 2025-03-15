class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        nums.sort()
      
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1  # Reset count for the new element
            
            if count > len(nums) / 2:
                return nums[i]
        
        return nums[len(nums) // 2]  # Majority element is always in the middle after sorting
