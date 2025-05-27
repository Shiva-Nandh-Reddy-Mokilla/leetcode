class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        i=1
        n1=0
        n2=0
        while i<=n:
            if i%m!=0:
                n1+=i
            else:
                n2+=i
            i+=1
        return n1-n2



        