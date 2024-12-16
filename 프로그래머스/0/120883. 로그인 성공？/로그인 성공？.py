def solution(id_pw, db):
    for i, k in db:
        if id_pw[0] == i:
            if id_pw[1] == k:
                return "login"
            else: 
                return "wrong pw"
    return "fail"
