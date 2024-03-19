import heapq
def solution(operations):
    heap = []
    for o in operations:
        op, v = o.split()
        if op == "I":
            heapq.heappush(heap, int(v))
        elif op == "D" and heap:
            heap.pop() if v == "1" else heap.pop(0) 
    return [max(heap), min(heap)] if heap else [0, 0]