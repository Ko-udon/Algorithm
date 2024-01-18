def solution(my_string, alp):
    for i, s in enumerate(my_string):
        if s == alp:
            my_string = my_string.replace(s, s.upper())
    return my_string