def solution(people, limit):
    # 투 포인터
    group = 0
    
    left, right = 0, len(people) - 1
    people.sort()
    while left < right:
        # 조건에 해당하다면 두명이 그룹으로 탑승
        if people[left] + people[right] <= limit:
            left += 1 
            group += 1 
        right -= 1
    # 전체 길이에서 그룹으로 탑승한 경우의 수를 빼주면 구명보트의 개수
    return len(people) - group