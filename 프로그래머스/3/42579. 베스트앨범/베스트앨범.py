def solution(genres, plays):
    answer = []
    genres_count = {}
    for i in range(len(plays)):
        genres_count[genres[i]] = genres_count.get(genres[i], 0) + plays[i]
    #print(genres_count)
    genres_count = sorted(genres_count.items(), key=lambda x:x[1], reverse=True)
    
    for k, v in genres_count:
        tmp = {}
        for i, g in enumerate(genres):
            if g == k:
                tmp[i] = tmp.get(i, 0) + plays[i]
        
        tmp = sorted(tmp.items(), key=lambda x:x[1], reverse=True)
        for i, p in tmp[:2]: # 장르별 최대 2개까지
            answer.append(i)
    
    return answer