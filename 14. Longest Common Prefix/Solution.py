class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:  # Check if the list is empty
            return ""

        res = ""
        # Loop through each character index of the first string
        for i in range(len(strs[0])):
            # Compare the character at index i of each string with the ith character of the first string
            for s in strs:
                # If index i is out of range for string s or characters differ
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            # If all strings have the same character at index i, add it to the result
            res += strs[0][i]
        return res