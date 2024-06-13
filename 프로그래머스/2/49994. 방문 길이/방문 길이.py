# def solution(dirs):
#     answer = set() # 중복제거
#     pos = [0,0] # 현재 위치

#     for d in dirs:
#         if d == 'U' and pos[1] < 5:
#             pos[1]+=1
#             now_pos = (pos[0], pos[1] - 0.1)
#         elif d == 'D' and pos[1] > -5:
#             pos[1]+=-1
#             now_pos = (pos[0], pos[1] + 0.1)
#         elif d == 'R' and pos[0] < 5:
#             pos[0]+=1
#             now_pos = (pos[0] - 0.1, pos[1])
#         elif d == 'L' and pos[0] > -5:
#             pos[0]+=-1
#             now_pos = (pos[0] + 0.1, pos[1])
#         else:
#             pass
#         answer.add(now_pos)
#     return len(answer)

def solution(dirs):
    s = set()
    d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x,y,nx,ny))
            s.add((nx,ny,x,y))
            x, y = nx, ny
    return len(s)//2