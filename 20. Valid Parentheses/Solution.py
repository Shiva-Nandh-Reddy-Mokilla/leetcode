class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        heap={')':'(',']':'[','}':'{'}
        for i in s:
            if i in heap:
                if stack and stack[-1]==heap[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if not stack:
            return True
        else:
            return False
                    