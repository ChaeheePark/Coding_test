x=int(input())
cnt=0
for i in range(x):
    word=input()
    
    for j in range(len(word)):
        if j<len(word)-1:
            if word[j] == word[j+1]:
                continue
            elif word[j] in word[j+1:]:
                break
        else:
            cnt+=1
print(cnt)
                
