# 답 참조
# 크루스칼..
def solution(n, costs):
    answer = 0
    uni = [0] * (n + 1)
    costs.sort(key = lambda x: x[2])
    for i in range(1,n + 1):
        uni[i] = i
        
    def union(x,y):
        a = find(x)
        b = find(y)
        if a != b:
            uni[a] = b
            
    def find(x):
        if uni[x] == x: return x
        else:
            uni[x] = find(uni[x])
            return uni[x]
        
        
    for n1,n2,cost in costs:
        if find(n1) != find(n2):
            union(n1,n2)
            answer += cost
            
    return answer

