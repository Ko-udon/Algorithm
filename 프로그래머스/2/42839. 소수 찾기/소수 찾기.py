from itertools import permutations
from collections import defaultdict

def is_prime(n):
    return all([(n%j) for j in range(2, int(n**0.5)+1)]) and n>1

def solution(numbers):
    count = 0
    history = []
    for n in range(len(numbers)):
        for digit_arr in permutations(numbers, n+1):
            number = 0

            for i, digit in enumerate(digit_arr):
                b = len(digit_arr) - i - 1
                number += int(digit) * (1*(10**b))

            if number not in history and is_prime(number):
                history.append(number)
                count+=1

    return count