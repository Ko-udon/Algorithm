def solution(myStr):
    seperate = ['a', 'b', 'c']
    for s in seperate:
        myStr = myStr.replace(s, ' ')
    answer = myStr.split()
    if answer == []:
        return ["EMPTY"]
    
    return answer