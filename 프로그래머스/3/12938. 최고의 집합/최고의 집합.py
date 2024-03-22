def solution(n, s):
    if s//n == 0:
        return [-1]

    answer = [s//n] * (n-s%n)
    answer2 = [(s//n)+1] * (s%n)
    answer.extend(answer2)
    return answer