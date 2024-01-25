def solution(friends, gifts):
    zero_list = [0] * len(friends)
    present_dict = {}
    for friend in friends:
        present_dict[friend] = [0] * len(friends)
    
    present_degree = dict(zip(friends,zero_list))
    
    
    for gift in gifts:
        give = gift.split(' ')[0] # 준사람
        get = gift.split(' ')[1] # 받은사람
        
        # 선물지수 계산
        present_degree[give] = present_degree.get(give) + 1
        present_degree[get] = present_degree.get(get) - 1
        
        # 친구별로 각자 선물 준 계수 계산
        present_dict[give][friends.index(get)] += 1
    
    result = dict(zip(friends,zero_list))
    for i in range(len(friends)):
        for j in range(i+1, len(friends)):
            
            
            # 주고받은 기록이 같다면
            if present_dict[friends[i]][friends.index(friends[j])] == present_dict[friends[j]][friends.index(friends[i])]:
                # 선물지수 비교
                if present_degree.get(friends[i]) > present_degree.get(friends[j]):
                    result[friends[i]] = result.get(friends[i]) + 1
                elif present_degree.get(friends[i]) < present_degree.get(friends[j]):
                    result[friends[j]] = result.get(friends[j]) + 1
            
            else:
                # 더 많이 준사람이 다음달에 받기
                if present_dict[friends[i]][friends.index(friends[j])] > present_dict[friends[j]][friends.index(friends[i])]:
                    result[friends[i]] = result.get(friends[i]) + 1
                else:
                    result[friends[j]] = result.get(friends[j]) + 1
            
    return max(result.values())
                
            
    
        