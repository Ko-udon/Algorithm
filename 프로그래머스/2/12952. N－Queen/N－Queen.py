# 문제 너무 어렵다...
# https://ye0nn.tistory.com/43 님의 답
def nqueen(queens, next_queen, n):
    global answer

    if next_queen in queens:  # 같은 행에 있는지 체크
        return

    for row, col in enumerate(queens):
        next_queen_row = len(queens)
        if abs(next_queen - col) == next_queen_row - row:  # 대각선에 있는지 체크
            return

    queens.append(next_queen)

    if len(queens) == n:
        answer += 1
        return

    for next_queen in range(n):
        nqueen(queens[:], next_queen, n)


def solution(n):
    global answer
    answer = 0

    for next_queen in range(n):
        queens = []
        nqueen(queens, next_queen, n)

    return answer