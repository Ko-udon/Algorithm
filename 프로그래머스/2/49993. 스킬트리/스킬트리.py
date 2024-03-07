def solution(skill, skill_trees):
    answer = 0
    skill_arr = list(skill)
    for st in skill_trees:
        tmp = ""
        for s in st:
            if s in skill:
                tmp += s
        if tmp == skill[:len(tmp)]:
            answer += 1
    return answer