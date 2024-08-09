def solution(s):
    s = list(s)
    s.sort()
    s.reverse()
    return "".join(s)
# 
def solution(s):
    s = list(s)
    s = sorted(s, reverse=True)
    return "".join(s)