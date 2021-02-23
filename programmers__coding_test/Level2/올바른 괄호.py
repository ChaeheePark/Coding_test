def solution(s):
    scount=0
    for i in s:
        if i=="(":
            scount+=1
        else:
            if scount>=1:
                scount-=1
            else:
                return False
    if scount==0:
        return True
    else:
        return False
