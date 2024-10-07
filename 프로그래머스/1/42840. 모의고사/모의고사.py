a = [1, 2, 3, 4, 5]
b = [2, 1, 2, 3, 2, 4, 2, 5]
c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]



def solution(answers):
    answer = []
    aa = [1 for i, val in enumerate(answers) if a[i % 5] == val]
    bb = [1 for i, val in enumerate(answers) if b[i % 8] == val]
    cc = [1 for i, val in enumerate(answers) if c[i % 10] == val]

    x = max([len(aa),len(bb),len(cc)])

    if x == len(aa) :
        answer.append(1)
    if x == len(bb) :
        answer.append(2)
    if x == len(cc) :
        answer.append(3)

    sorted(answer)

    return answer