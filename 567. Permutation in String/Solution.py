class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1,n2=len(s1),len(s2)
        if n1>n2:
            return False
        freq1,freq2=Counter(s1),Counter(s2[0:n1])
        if freq1==freq2: return True
        l=1
        r=n1
        while r<n2:
            freq2[s2[l-1]]-=1
            freq2[s2[r]]+=1
            r+=1
            l+=1
            if freq1==freq2:
                return True
        return False
        


        
