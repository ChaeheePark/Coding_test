def solution(n, m):
    answer = []
    maxn=m
    if n>m:
        maxn=n
    k1=1 #최대공약수
    k2=1 #최소공배수
    for i in range(maxn+1,1,-1):
        if n%i ==0 and m%i==0:
            k1=i
            break
    k2=n*m // k1
    answer.append(k1)
    answer.append(k2)
    return answer
