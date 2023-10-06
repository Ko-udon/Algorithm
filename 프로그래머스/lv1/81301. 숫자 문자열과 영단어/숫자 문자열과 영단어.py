def solution(s):
    numbers = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for n in range(len(numbers)):
        s = s.replace(numbers[n], str(n))
    return int(s)
    