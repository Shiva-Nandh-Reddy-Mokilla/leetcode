class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maximum=0
        minimum=prices[0]
        for i in prices:
            if minimum>i:
                minimum=i
            if maximum<(i-minimum):
                maximum=i-minimum


            minimum=min(minimum,i)
            maximum=max(maximum,i-minimum)
        return maximum
    

