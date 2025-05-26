class Solution:
    def findMin(self, nums: List[int]) -> int:
        min=nums[0]
        i=1
        for i in nums:
            if i<min:
                min=i
            else:
                continue
        return min
        

        
        