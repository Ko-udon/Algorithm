def solution(spell, dic):
    for s in dic:
        if set(spell) - set(s) == set():
            return 1
    return 2