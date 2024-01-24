def solution(n):
    # 좌표 및 방향 정보
    x_idx, y_idx = 0, 0
    direction = "right"
    directions = ["right", "down", "left", "top", "right"]

    # 배열 초기화 (0으로)
    L = [[0 for _ in range(n)] for __ in range(n)]

    # n x n 반복
    for num in range(1, n * n + 1):

        # 값 대입
        L[x_idx][y_idx] = num


        # 방향이 오른쪽인 경우
        if direction == "right":

            # 해당 조건 만족 시 방향 전환, 아니면 인덱스 증가
            if y_idx + 1 == n or L[x_idx][y_idx + 1] != 0:
                direction = "down"
                x_idx += 1
            else:
                y_idx += 1

        # 방향이 아래쪽인 경우
        elif direction == "down":

            # 해당 조건 만족 시 방향 전환, 아니면 인덱스 증가
            if x_idx + 1 == n or L[x_idx + 1][y_idx] != 0:
                direction = "left"
                y_idx -= 1
            else:
                x_idx += 1

        # 방향이 왼쪽인 경우
        elif direction == "left":

            # 해당 조건 만족 시 방향 전환, 아니면 인덱스 증가
            if L[x_idx][y_idx - 1] != 0:
                direction = "top"
                x_idx -= 1
            else:
                y_idx -= 1

        # 방향이 위쪽인 경우
        elif direction == "top":

            # 해당 조건 만족 시 방향 전환, 아니면 인덱스 증가
            if L[x_idx - 1][y_idx] != 0:
                direction = "right"
                y_idx += 1
            else:
                x_idx -= 1
    return L