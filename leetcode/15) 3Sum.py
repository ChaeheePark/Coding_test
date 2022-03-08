class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output=set()
        pos=sorted([n for n in nums if n>0])
        pos_set=set(pos)
        neg=sorted([n for n in nums if n<0])
        neg_set=set(neg)
        zeros=[n for n in nums if n==0]
        
        #모두 0
        if len(zeros)>=3:
            output.add((0,0,0))
        
        #-1+0+1
        if len(zeros)>0:
            for i in pos:
                if -i in neg_set:
                    output.add((-i,0,i))
        i=0
        j=0
        #-1+-1+2
        for i in range(len(neg)):  
            for j in range(i+1,len(neg)):
                tp=-(neg[i]+neg[j])
                if tp in pos_set:
                    output.add((neg[i],neg[j],tp))
                
        i=0
        j=0
        #1+1-2
        for i in range(len(pos)):
            for j in range(i+1,len(pos)):
                tp=-(pos[i]+pos[j])
                if tp in neg_set:
                    output.add((pos[i],pos[j],tp))
                    
        return list(output)
