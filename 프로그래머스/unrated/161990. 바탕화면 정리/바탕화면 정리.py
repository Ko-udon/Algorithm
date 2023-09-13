def solution(wallpaper):
    answer = []
    a, b = [], []
    
    #wallpaper 내부 전체 돌면서
    for i in range(len(wallpaper)): 
        for j in range(len(wallpaper[0])):
            if(wallpaper[i][j]=="#"):
                a.append(i)
                b.append(j)
    #와
    return (min(a), min(b), max(a)+1, max(b)+1)