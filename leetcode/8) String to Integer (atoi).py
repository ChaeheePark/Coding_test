import re

class Solution:
    def myAtoi(self, s: str) -> int:
        
        output=0
        
        s=s.strip()
        
        if s=="":
            output=0
        else:
            
            num_list=re.findall(r"^[-+]?[0-9]+",s)
            
            if len(num_list)==0:
                output=0
            else:
                num=int(num_list[0])
                if num>2**31-1:
                    num=2**31-1
                elif num<-2**31:
                    num=-2**31
                output=num
        return output
