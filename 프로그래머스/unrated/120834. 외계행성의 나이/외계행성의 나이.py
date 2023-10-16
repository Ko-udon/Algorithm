def solution(age):
    age_alpha = 'abcdefghij'
    a = list(map(int, str(age)))
    return ''.join(age_alpha[i] for i in a)