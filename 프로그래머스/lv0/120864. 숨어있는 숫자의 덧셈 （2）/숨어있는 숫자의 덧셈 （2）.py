import re
def solution(my_string):
    s = re.findall(r'[0-9]+', my_string)
    return sum(list(map(lambda x: int(x), s)))
    