class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        nums={"0":0, "1":1, "2":2, "3":3,"4":4,"5":5, "6":6,"7":7,"8":8,"9":9}
        num1_int=0
        num2_int=0
        
        for i in range(len(num1),0,-1):
            num1_int+=nums[num1[i-1]]*10**(len(num1)-i)
            
        for i in range(len(num2),0,-1):
            num2_int+=nums[num2[i-1]]*10**(len(num2)-i)
    
        return str(num1_int*num2_int)
