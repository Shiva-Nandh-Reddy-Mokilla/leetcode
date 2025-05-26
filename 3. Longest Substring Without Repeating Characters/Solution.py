class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h={}
        maximum=0
        start=0
        for i,num in enumerate(s):
            if num in h and h[num]>=start:
                start=h[num]+1
            h[num]=i
            maximum=max(maximum,i-start+1)
        return maximum
        
        