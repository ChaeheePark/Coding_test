def solution(skill, skill_trees):
    answer=0
    for i in range(len(skill_trees)):
        t=skill_trees[i]
        temp=[]
        for j in range(len(t)):
            if t[j] in skill:
                temp.append(t[j])
        print(temp)
        k=0
        flag=True
        for j in range(len(temp)):
            if temp[j]!=skill[k]:
                flag=False
            k+=1
        print(flag)
        if flag:
            answer+=1
    return answer
