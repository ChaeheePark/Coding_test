import heapq

def solution(scoville, K):
    heap=[]
    for t in scoville:
        heapq.heappush(heap, t)
    count=0
    while heap[0]<K:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        except IndexError:
            return -1
        count += 1
    return count
