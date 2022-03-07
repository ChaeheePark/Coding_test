class Solution:
    def intToRoman(self, num: int) -> str:
        
        rom_dict={"M":1000,"CM":900,"D":500,"CD":400,"C":100, "XC":90, "L":50,"XL":40, "X":10,"IX":9, "V":5,"IV":4,"I":1}
        
        output=''
        while num!=0:
            for i in rom_dict:
                if num-rom_dict[i]>=0:
                    output+=i
                    num-=rom_dict[i]
                    break
            #print(num)
        return output
                    
