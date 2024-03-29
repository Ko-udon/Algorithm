import heapq
def solution(n, works):
    if sum(works) <= n:
        return 0
    works = [-work for work in works]
    heapq.heapify(works)
    print(works)
    for _ in range(n):
        work = heapq.heappop(works) + 1
        heapq.heappush(works, work)
    
    return sum([w**2 for w in works])