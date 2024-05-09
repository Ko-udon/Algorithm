def solution(s):
    answer = ''
    l = s.split(" ")
    for i, word in enumerate(l):
        # 첫 단어가 글자이고 빈칸이 아닌 경우
        if word and not word.isdigit():
            f = word[0].upper()
            b = word[1:].lower()
            l[i] = f + b
    return ' '.join(l)
    