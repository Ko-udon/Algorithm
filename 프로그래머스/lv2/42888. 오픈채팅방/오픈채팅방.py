def solution(record):
    userinfo = {}
    answer = []
    
    for text in record:
        info = text.split(' ')
        if info[0] == 'Enter':
            userinfo.update({info[1]:info[2]})
        elif info[0] == 'Change':
            userinfo.update({info[1]:info[2]})

    for text in record:
        info = text.split(' ')
        if info[0] == 'Enter':
            answer.append(f'{userinfo[info[1]]}님이 들어왔습니다.')
        elif info[0] == 'Leave':
            answer.append(f'{userinfo[info[1]]}님이 나갔습니다.')
    return answer