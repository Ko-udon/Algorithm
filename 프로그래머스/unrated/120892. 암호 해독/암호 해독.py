def solution(cipher, code):
    answer = ''.join(cipher[code - 1::code])
    return answer