from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numbers={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        tp=[]
        output=[]
        if digits=="":
            return output
        for i in range(len(digits)):
            tp.append(numbers[digits[i]])
        ttp=tuple(product(*tp))
        
        for i in range(len(ttp)):
            a=''
            for j in range(len(ttp[i])):
                a+=str(ttp[i][j])
            output.append(a)
        return output
        
            
