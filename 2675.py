x=int(input())
for i in range(x):
    t=input()
    answer=""
    t=t.split(" ",2)
    
    string=t[1]
    for k in range(len(string)):
         answer+=string[k]*int(t[0])
    print(answer)
