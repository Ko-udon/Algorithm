import heapq

def solution(scoville, K):
    answer = 0
    heap = []

    for s in scoville:
        heapq.heappush(heap, s)
    while heap[0] < K:
        if len(heap) == 1:
            return -1

        n = heapq.heappop(heap)
        t = heapq.heappop(heap)
        heapq.heappush(heap, n + (t * 2))
        answer += 1

    return answer
