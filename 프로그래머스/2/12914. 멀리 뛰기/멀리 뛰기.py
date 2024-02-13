def solution(n):
    # 배열 싹다 0으로 초기화
    arr = [0 for i in range(2001)]
    arr[1] = 1 # 1칸짜리 경우의수는 1개
    arr[2] = 2 # 2칸짜피 경우의수는 1칸, 1칸 또는 2칸 으로 2개
    
    for i in range(3, 2001):
        arr[i] = (arr[i-1] + arr[i-2]) % 1234567
    return arr[n]