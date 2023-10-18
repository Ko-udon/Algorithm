def solution(my_string):
    answer = []
    for s in my_string:
        if str.isdigit(s):
            answer.append(int(s))
            
    return sorted(answer)