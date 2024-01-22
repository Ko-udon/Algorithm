def solution(rank, attendance):
    list_dic = dict(zip(rank, attendance))
    list_dic = sorted(list_dic.items())
    attendance_list = []
    for l in list_dic:
        if l[1] == True:
            attendance_list.append(rank.index(l[0]))
            if len(attendance_list) == 3:
                break
    
    a, b, c = attendance_list
    return (10000 * a) + (100 * b) + c