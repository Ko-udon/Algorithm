def solution(myString):
    answer = ' '.join(myString.split('x')).split()
    return sorted(answer)
    