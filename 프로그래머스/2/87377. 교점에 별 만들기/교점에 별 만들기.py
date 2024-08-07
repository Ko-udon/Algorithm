# 역행렬 문제... 생각해내기 쉽지 않음
# 많이 어려웠다, 풀이 실패

def solution(line):
    inters = []

    for a in line:
        for b in line:
            if a == b: # 같은 직선이면 패스
                continue
            inter = find_intersection(a, b) # 다른경우, 두 직선의 교차점 찾기
            if inter:
                inters.append(inter)

    inters = list(set(map(lambda x: (int(x[0]), int(x[1])), inters)))

    return display_coordinates(inters) # 별로 그리기


# 교차점 찾는 함수
def find_intersection(s, t):
    a, b, e = s # 첫번째 직선의 x, y계수, 상수
    c, d, f = t # 두번쨰 직선의 ,,

    # 교점 구하기
    deter = a*d-b*c

    if deter == 0:
        return None

    x = (b*f-e*d) / (a*d-b*c) # 역행렬 이용
    y = (e*c-a*f) / (a*d-b*c)

    if x != int(x) or y != int(y):
        return None

    return [x, y]


# 결과값을 별로 그리는 함수
# 
def display_coordinates(coordinates):
    # 좌표 중 최대값과 최소값을 찾아 배열의 크기를 결정
    min_x = min(x for x, _ in coordinates)
    max_x = max(x for x, _ in coordinates)
    min_y = min(y for _, y in coordinates)
    max_y = max(y for _, y in coordinates)
    size_x = max_x - min_x + 1
    size_y = max_y - min_y + 1

    grid = [['.' for _ in range(size_x)] for _ in range(size_y)]

    for x, y in coordinates:
        grid[max_y - y][x - min_x] = '*'

    result = [''.join(row) for row in grid]
    return result

