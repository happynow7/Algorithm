def solution(rsp):
    sol = {'2':'0', '0':'5', '5':'2'}

    return ''.join(sol[i] for i in rsp)