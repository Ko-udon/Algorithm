def solution(num_list):
    odd_sum = sum[(num_list[n] for n in range(0, len(num_list), 1))]
    even_sum = sum[(num_list[n] for n in range(1, len(num_list), 1))]
    return odd_sum if odd_sum >= even_sum else even_sum