class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle not in haystack:
            return -1
        if len(needle)>len(haystack):
            return -1
        
        for i in range(len(haystack)-len(needle)+1):
            count=0
            for j in range(len(needle)):
                if needle[j]==haystack[i+j]:
                    count+=1
                else:
                    break
            if count==len(needle):
                return i

        return -1