class Solution:
    def reverse(self, x: int) -> int:
        output=0
        if x<0 and x>=-2**31:
            x=abs(x)
            t=str(x)
            t=t[::-1]
            output=-int(t)
        elif x>0 and x<=2**31-1:
            print(2**31-1)
            t=str(x)
            t=t[::-1]
            output=int(t)
            
        if output >2**31 or output<=-2**31-1 or output==0:
            return 0
        else:
            return output
     
