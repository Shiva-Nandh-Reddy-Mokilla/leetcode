class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1

        while low<=high:
            if nums[low]==target:
                return low
            if nums[high]==target:
                return high
            low+=1
            high-=1
        return -1

        