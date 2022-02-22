class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp=set()
        output=0
        t=0
        
        for i in range(len(s)):
            while s[i] in temp:
                temp.remove(s[t])
                t+=1
                      
            temp.add(s[i])
            output=max(output,i-t+1)
            
        return output
