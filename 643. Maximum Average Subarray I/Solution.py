class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        c_sum=sum(nums[:k])
        max_sum=c_sum

        for i in range(k,len(nums)):
            c_sum=c_sum+nums[i]-nums[i-k]
            max_sum=max(max_sum,c_sum)
        return float(max_sum) / k
    
           