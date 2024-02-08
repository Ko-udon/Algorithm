def solution(n, words):
    count_turn = {}
    for i in range(n):
        count_turn[i] = 0
    word_list = []
    word = ''
    
    for i, w in enumerate(words):
        turn = i%n
        if (word!='' and word[-1] != w[0]) or w in word_list:
            return [turn + 1, count_turn[turn] + 1]
        count_turn[turn] = count_turn.get(turn) + 1
        word = w
        word_list.append(w)
    return [0, 0]