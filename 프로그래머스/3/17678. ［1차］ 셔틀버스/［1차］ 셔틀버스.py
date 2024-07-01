def solution(n, t, m, timetable):
    timetable = sorted([int(i[:2])*60+int(i[-2:]) for i in timetable], reverse=True)
    bus_time = 9*60 -t
    
    for i in range(n-1): 
        bus_time += t 
        for _ in range(m): 
            if timetable and timetable[-1]<=bus_time:
                timetable.pop()
            else: 
                break

    bus_time += t 
    my_time = bus_time if len(timetable)<m or timetable[-m]>bus_time else timetable[-m] -1
    
    return f'{my_time//60:02d}:{my_time%60:02d}'