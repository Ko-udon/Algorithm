# def solution(numbers):
#     numbers_str = list(map(str, numbers))
#     print(numbers_str)
    
#     # 문자열 비교를 통해 정렬, 1000까지라서 x*3
#     # 근데 이걸 생각해내기 쉽지 않을듯...
#     numbers_str.sort(key=lambda x: x*3, reverse=True)
#     print(numbers_str)
    
#     answer = ''.join(numbers_str)
#     print(answer)
#     return str(int(answer))

import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer