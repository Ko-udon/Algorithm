# 문제에 모든 달은 28일 까지 있다고 가정
def turnDate(date):
    year, month, day = map(int, date.split("."))
    return year * 28 * 12 + month * 28 + day

def solution(today, terms, privacies):
    answer = []
    term = dict(zip(list(map(lambda x : x[0],terms)),list(map(lambda x : x[2:],terms))))
    i = 1
    
    for p in privacies:
        turnDate(str(p.split(" ")[0]))
        
        if turnDate(p.split()[0]) + int(term.get(p.split()[1])) * 28 <= turnDate(today):
            answer.append(i)
        i+=1
        
    
    
    return answer