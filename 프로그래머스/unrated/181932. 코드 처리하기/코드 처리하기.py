def solution(code):
    mode = 0
    ret = ''
    for i in range(0, len(code)):
        if code[i] == "1" or code[i] == "0":
            mode = switchMode(mode)
            continue
            
        if mode == 0:
            if i%2 == 0:
                ret += code[i]
        elif mode == 1:
            if i%2 != 0:
                ret += code[i]
    if ret == '':
        return "EMPTY"
    return ret

def switchMode(mode):
    if mode == 0:
        mode = 1
    else:
        mode = 0
    return mode