from math import factorial
def solution(n, k):
    answer = []
    order = list(range(1,n+1))
    while n!=0 :
        fact = factorial(n-1)
        answer.append(order.pop((k-1)//fact))
        n,k = n-1, k%fact
    return answer