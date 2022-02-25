class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        temp = [[] for _ in range(numRows)]
        
        idx=0
        down=1
        
        if numRows==1:
            return s
        
        for i in range(len(s)):
            if down==1:
                if idx<numRows:
                    temp[idx].append(s[i])
                    idx+=1
                if idx==numRows:
                    idx-=2
                    down=0
            
            else:
                if idx<numRows:
                    temp[idx].append(s[i])
                    idx-=1
                if idx==-1:
                    idx+=2
                    down=1
            
        output=''
        
        for i in range(numRows):
            output += ''.join(temp[i])       
        return output
                
