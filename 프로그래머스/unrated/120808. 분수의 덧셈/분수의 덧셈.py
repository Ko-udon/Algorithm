import math

def lcm(a, b):
    return a * b / math.gcd(a, b)

def solution(numer1, denom1, numer2, denom2):
    l = int(lcm(denom1, denom2))
    r = int(numer1*(l/denom1) + numer2*(l/denom2))
    m = math.gcd(l,r)
    answer = [r/m,l/m]
    return answer
