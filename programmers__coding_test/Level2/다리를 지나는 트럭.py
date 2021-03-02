def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue=[0]*bridge_length
    truck_copy=truck_weights.copy()
    
    while len(queue)>0:
        queue.pop(0)
        if len(truck_weights)>0:
            if sum(queue)+truck_weights[0]<=weight:
                queue.append(truck_weights.pop(0))
            else:
                queue.append(0)
        answer+=1
    return answer
