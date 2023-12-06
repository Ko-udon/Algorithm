def solution(board, h, w):
    answer = 0
    color = board[h][w]
    
    li = checkCount(h,w,len(board))
            
    for l in li:
        if color == board[l[0]][l[1]]:
            answer +=1
            
    return answer

def checkCount(h,w,size):
    checkList = []

    if h-1 > -1:
        checkList.append([h-1,w])
        
    if (w-1>-1):
        checkList.append([h,w-1])
    
    if (w+1<size):
        checkList.append([h,w+1])
    
    if (h+1<size):
        checkList.append([h+1,w])
    
    
    return checkList