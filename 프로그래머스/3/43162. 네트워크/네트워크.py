def solution(n, computers):
    def dfs(v):
        visited[v] = True
        for i in range(n):    # 인접노드 탐구 
            if not visited[i] and computers[v][i]:    # unvisited + 인접할 때 
                dfs(i)

    count = 0   # 네트워크 수
    visited = [False] * (n)   

    for node in range(n):
        if not visited[node]:
            dfs(node)
            count += 1
    return count