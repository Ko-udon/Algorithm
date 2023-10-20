def solution(my_string, num1, num2):
    s_arr = list(my_string)
    s_arr[num1], s_arr[num2] = s_arr[num2], s_arr[num1]
    return ''.join(s_arr)