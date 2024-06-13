# level2?...
def solution(maps):
    answer = []
    N = len(maps)
    M = len(maps[0])
    visited = [[False]*M for _ in range(N)]
    delta = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(N):
        for j in range(M):
            if maps[i][j] != 'X' and not visited[i][j]:
                food = 0
                stack = [(i,j)]
                while stack:
                    x,y = stack.pop()
                    if visited[x][y]:   continue
                    visited[x][y] = True
                    food += int(maps[x][y])
                    for dx,dy in delta:
                        if 0 <= x+dx <= N-1 and 0 <= y+dy <= M-1 and maps[x+dx][y+dy] != 'X':
                            stack.append((x+dx,y+dy))
                answer.append(food)
    if answer:
        return sorted(answer)
    else:
        return [-1]