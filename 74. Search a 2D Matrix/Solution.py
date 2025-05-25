class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left=0
        right=len(matrix)-1
        
        while left<=right:
            mid=(left+right)//2
            if matrix[mid][0]>target:
                right=mid-1
            elif matrix[mid][-1]<target:
                left=mid+1
            else:
                break
        i=matrix[mid]
        l=0
        h=len(i)-1
        if target not in i:
            return False
        while l<=h:
            m=(l+h)//2
            if i[m]>target:
                h=m-1
            elif i[m]<target:
                l=m+1
            else:
                return True

        
        