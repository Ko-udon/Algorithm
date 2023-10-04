def solution(id_list, report, k):
    answer = []

    # 신고 결과에 따라 메일 받을 횟수를 담을 dict
    user_result = {}
    for user in id_list:
        user_result[user] = 0

    # 신고 결과 담을 dict
    user_map = {}
    for user in id_list:
        user_map[user] = []
    for r in report:
        li = r.split(' ')
        user_map[li[1]].append(li[0])
    
    # 신고 받은 횟수가 k 이상인 유저들만 정지 대상으로 판별
    for key, value in user_map.items():
        if len(set(value)) >= k:
            for v in set(value):
                user_result[v]+=1

    
    return list(user_result.values())