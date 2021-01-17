
def solution(participant, completion):
    answer = ''
    dict1 = {}
    for p in participant:
        if p not in dict1:
            dict1[p] = 0
        if p in dict1:
            dict1[p] = dict1.get(p) + 1
    for c in completion:
        dict1[c] = dict1.get(c)-1
    for p in participant:
        if dict1[p] == 1:
            answer = p
    return answer
