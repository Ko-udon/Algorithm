# 깔끔한 풀이법 대단하다 ㄷㄷ..
def solution(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)]
            temp_list.append(f'({b.join(temp)})')
        # print(temp_list)
        answer.append(abs(eval(a.join(temp_list)))) # eval은 수식으로 구성된 문자열을 연산해줌
    return max(answer)