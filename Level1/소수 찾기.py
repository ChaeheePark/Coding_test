def solution(n):
    # 에라토스테네스의 체 
    sieve = [True] * (n+1)

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           
            for j in range(i+i,n+1, i): 
                sieve[j] = False
    count=0
    for i in range(2, n+1):
        if sieve[i] == True:
            count+=1

    return count
