def solution(mats, park):
    row = len(park)
    col = len(park[0])
    max_size = -1
    mats.sort()
    
    for m in reversed(mats):
        is_ = False

        for i in range(row - m + 1):
            for j in range(col - m + 1):
                is_minus = True

                for x in range(i, i + m):
                    for y in range(j, j + m):
                        if park[x][y] != '-1':
                            is_minus = False
                            break
                    if not is_minus:
                        break
                if is_minus:
                    is_ = True
                    break
            if is_:
                break
        if is_:
            max_size = m
            break  

    return max_size
