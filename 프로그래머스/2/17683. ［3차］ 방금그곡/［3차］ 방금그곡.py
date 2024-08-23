def solution(m, musicinfos): # split, replace 많이 쓰는 문제
    answer = '(None)'
    m = m.replace('A#', 'H').replace('C#', 'I').replace('D#', 'J').replace('F#', 'K').replace('G#', 'L').replace('B#', 'M') # 문제조건에 없는 B#...
    max_time = 0
    for info in musicinfos:
        start, end, title, melody = info.split(',')
        start = start.split(':')
        end = end.split(':')
        time = (int(end[0]) - int(start[0])) * 60 + int(end[1]) - int(start[1])
        
        melody = melody.replace('A#', 'H').replace('C#', 'I').replace('D#', 'J').replace('F#', 'K').replace('G#', 'L').replace('B#', 'M') # 문제 조건에 B#은 없다... 문제 오류인듯 34번 테스트케이스 
        melody = melody * (time // len(melody)) + melody[0:time % len(melody)]
        if m in melody and time > max_time:
            max_time = time
            answer = title
    return answer