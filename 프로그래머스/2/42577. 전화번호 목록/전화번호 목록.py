def solution(phoneBook):
    
    sort_phoneBook= sorted(phoneBook)
    for p1, p2 in zip(sort_phoneBook, sort_phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True