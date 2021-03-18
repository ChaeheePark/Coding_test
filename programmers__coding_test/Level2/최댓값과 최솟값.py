def solution(s):
    li=s.split(" ")
    
    for i in range(len(li)):
        li[i]=int(li[i])
    a= str(min(li))+" "+str(max(li))
    return a
