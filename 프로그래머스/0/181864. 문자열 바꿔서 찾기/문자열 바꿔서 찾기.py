def solution(myString, pat):
    change = ''
    for s in pat:
        if s == "A":
            change += "B"
        else:
            change += "A"
    if change in myString:
        return 1
    return 0