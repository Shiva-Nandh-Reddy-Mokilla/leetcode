class Solution(object):
    def minMaxDifference(self, num):
        """
        :type num: int
        :rtype: int
        """
        number=str(num)
        temp=''
        stri=''
        strj=''
        for i in number:
            if i!='9':
                temp=i
                break
        for i in number:
            first=i
            break
            
        
        for i in number:
            
            if i==temp:
                stri+='9'
        
            else:
                stri+=i
            if i==first:
                strj+='0'
        
            else:
                strj+=i
 
                
        return int(stri)-int(strj)

        
        
   
        