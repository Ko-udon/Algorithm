def solution(id_pw, db):
    user_info = {}
    for i in db:
        user_info[i[0]] = i[1]

    if user_info.get(id_pw[0]) == None:
        return "fail"
    elif user_info[id_pw[0]] == id_pw[1]:
        return "login"
    else:
        return "wrong pw"
        

    