def solution(genres, plays):
    answer = []
    genres_count = {}
    for i in range(len(plays)): # 장르: 플레이수 dict
        genres_count[genres[i]] = genres_count.get(genres[i], 0) + plays[i]
    # 플레이 수 순으로 정렬
    genres_count = sorted(genres_count.items(), key=lambda x:x[1], reverse=True)

    for k, v in genres_count:
        tmp = {} # 장르별로 담을 임시 dict, 노래번호: 플레이 수
        for i, g in enumerate(genres):
            if g == k: 
                tmp[i] = tmp.get(i, 0) + plays[i]
        # 각 장르별로도 역시 플레이 수 순으로 정렬
        tmp = sorted(tmp.items(), key=lambda x:x[1], reverse=True)
        for i, p in tmp[:2]: # 장르별 최대 2곡까지 저장
            answer.append(i)
    return answer