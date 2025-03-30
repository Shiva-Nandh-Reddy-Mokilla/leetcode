class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numset=set(nums)
        countmax=0
        length=0
        if not nums:
            return 0


        for num in numset:
            if (num-1) not in numset:
                length=1
                while num+length in numset:
                    length+=1
                countmax=max(length,countmax)

            
        return countmax

    