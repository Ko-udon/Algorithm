def solution(players, callings):
    answer = []
    player_ranking = {}
    ranking_player = {}
    n = 0
    for p in players:
        player_ranking[p] = n
        ranking_player[n] = p
        n+=1

    for c in callings:
        num = player_ranking[c]
        front_player = ranking_player[num-1]
        
        
        ranking_player[num-1], ranking_player[num] = ranking_player[num], ranking_player[num-1]
        player_ranking[front_player], player_ranking[c] = player_ranking[c], player_ranking[front_player]
        
        

        
    return list(ranking_player.values())