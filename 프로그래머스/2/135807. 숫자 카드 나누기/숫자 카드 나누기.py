import math
def solution(arrayA, arrayB):
    gcd_1 = arrayA[0]
    gcd_2 = arrayB[0]
    for i in range(1, len(arrayA)):
        gcd_1 = math.gcd(arrayA[i], gcd_1)
        gcd_2 = math.gcd(arrayB[i], gcd_2)
        
    gcd_1, gcd_2 = check(arrayB, gcd_1), check(arrayA, gcd_2)

    if not (gcd_1 or gcd_2):
        return 0
    return max(gcd_1, gcd_2)
    
def check(arr, gcd):
    for a in arr:
        if a%gcd == 0:
            return 0
    return gcd # 전부 다 안나눠질 경우, 합격