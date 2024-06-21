def solution(phoneBook): 
    pb = sorted(phoneBook)
    for i in range(len(phoneBook)-1):
        if pb[i+1].startswith(pb[i]):
            return False
    return True
        
        