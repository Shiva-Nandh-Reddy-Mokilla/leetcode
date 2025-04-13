class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        numbers.sort()
        low=0
        high=len(numbers)-1
        while low < high:
            curr_sum = numbers[low] + numbers[high]
            if curr_sum == target:
                return [low + 1, high + 1]  # 1-based index
            elif curr_sum < target:
                low += 1
            else:
                high -= 1
            
        