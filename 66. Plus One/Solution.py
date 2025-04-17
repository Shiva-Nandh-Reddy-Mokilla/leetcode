class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s="".join(map(str,digits))
        n=int(s)
        n=n+1
        nlist=list(map(int,str(n)))
        return nlist



        