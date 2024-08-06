def solution(s):
    answer = ''
    sp = s.split(' ')
    for i in range(len(sp)):
        sp[i] = sp[i].capitalize()
    answer = ' '.join(sp)
    return answer