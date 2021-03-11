x=int(input())
s=list(str(x))

s.sort(reverse=True)

for i in s:
    print(i,end="")
