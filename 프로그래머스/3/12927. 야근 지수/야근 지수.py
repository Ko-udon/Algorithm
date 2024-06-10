import heapq
def solution(n, works):
    
    if sum(works) <= n:
        return 0
    
    works = [-i for i in works]
    heapq.heapify(works)
    
    for i in range(n):
        work = heapq.heappop(works)
        work += 1
        heapq.heappush(works, work)
        
    return sum([i**2 for i in works])