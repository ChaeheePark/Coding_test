from itertools import permutations

def solution(numbers):
    li=[]
    for i in range(1,len(numbers)+1):
        for j in permutations(list(numbers),i):
            t=int(''.join(j))
            for k in range(2,t):
                if t%k==0:
                    break
            else:
                if t not in li and t!=0 and t!=1:
                        li.append(t)
    return len(li)
            
