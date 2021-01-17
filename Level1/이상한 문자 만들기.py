def solution(s):
    answer=''
    
    strings=list(s)
    j=0
    for i in range(len(strings)):
        if strings[i]==" ":
            j=0
            continue;
        if j%2==0:
            strings[i]=strings[i].upper()
        else:
            strings[i]=strings[i].lower()
        j+=1
    print(strings)
    answer=(''.join(str(i) for i in strings))
    return answer
