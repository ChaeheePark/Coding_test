x=int(input())
for i in range(x):
    list=input()
    sum=0
    tp=0
    for j in range(len(list)):
        if list[j]=='O':
            tp+=1
            sum+=tp
        else:
            tp=0
    print(sum)
    

