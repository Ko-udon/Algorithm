import re

def solution(new_id):
    answer = new_id
    answer = answer.lower() # 1단계
    answer = re.sub('[^a-z0-9\-_.]', '', answer) # 2단계
    answer = re.sub('\.+', '.', answer) # 3단계
    answer = re.sub('^[.]|[.]$', '', answer) # 4단계
    answer = 'a' if len(answer) == 0 else answer[:15] # 5단계
    answer = re.sub('^[.]|[.]$', '', answer) # 6단계
    answer = answer if len(answer) >= 3 else answer + "".join([answer[-1] for i in range(3-len(answer))]) # 7단계

    return answer