class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res=defaultdict(list)
        for s in strs:
            sorteds=''.join(sorted(s))
            res[sorteds].append(s)
        return res.values()
    


        
        