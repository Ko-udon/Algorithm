def solution(players, callings):
    playerDict = {key: i for i, key in enumerate(players)}

    for c in callings:
        player = playerDict[c]
        playerDict[c] -= 1
        playerDict[players[player-1]] += 1
        players[player-1], players[player] = players[player], players[player-1]

    return players