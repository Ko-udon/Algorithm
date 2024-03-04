def solution(dirs):
    answer = set() # 중복제거
    pos = [0,0] # 현재 위치

    for d in dirs:
        if d == 'U' and pos[1] < 5:
            pos[1]+=1
            now_pos = (pos[0], pos[1] - 0.5)
        elif d == 'D' and pos[1] > -5:
            pos[1]+=-1
            now_pos = (pos[0], pos[1] + 0.5)
        elif d == 'R' and pos[0] < 5:
            pos[0]+=1
            now_pos = (pos[0] - 0.5, pos[1])
        elif d == 'L' and pos[0] > -5:
            pos[0]+=-1
            now_pos = (pos[0] + 0.5, pos[1])
        else:
            pass
        answer.add(now_pos)
    print(answer)
    return len(answer)