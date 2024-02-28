def solution(msg):
    answer = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dictionary = {k:v for (k,v) in zip(alphabet, list(range(1,27)))}

    while True:
        if msg in dictionary:
            answer.append(dictionary[msg])
            break
        for i in range(1, len(msg)+1):
            if msg[0:i] not in dictionary:
                answer.append(dictionary[msg[0:i-1]])
                dictionary[msg[0:i]] = len(dictionary)+1
                msg = msg[i-1:]
                break

    return answer