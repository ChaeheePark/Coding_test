def solution(x):
    sum=0
    list_x=list(str(x))
    for i in range(len(list_x)):
        sum+=int(list_x[i])
    if x%sum!=0:
        return False
    return True
