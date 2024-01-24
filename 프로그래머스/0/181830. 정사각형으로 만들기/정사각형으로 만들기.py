def solution(arr):
    row = len(arr)
    column = len(arr[0])
    
    if row ==column:
        return arr
    elif row > column:
        while row != column:
            for a in arr:
                a.append(0)
            column += 1
    else:
        while row != column:
            arr.append([0 for _ in range(column)])
            row += 1
    return arr
        