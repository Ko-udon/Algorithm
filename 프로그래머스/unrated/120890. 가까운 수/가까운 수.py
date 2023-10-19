def solution(array, n):
    array.append(n)
    array.sort()
    i = array.index(n)
    if i == 0:  # 배열 맨 앞일경우
        return array[1]
    elif i == len(array) - 1: # 배열 맨 뒤일경우
        return array[i - 1]
    else:
        return array[i-1] if abs(array[i-1] - n) <= abs(array[i+1] - n) else array[i+1]
    
    return answer