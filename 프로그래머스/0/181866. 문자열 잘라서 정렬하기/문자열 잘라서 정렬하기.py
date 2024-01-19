def solution(myString):
    answer = sorted([n for n in myString.split('x')])
    if "" in answer:
        answer = [value for value in answer if value != ""]
    return answer