def solution(s):
    answer = ''
    m = s.split(' ')
    for c in m:
        for k in range(len(c)):
            if k % 2 == 0:
                answer += c[k].upper()
            elif k % 2 != 0:
                answer += c[k].lower()
        answer += ' '
        
    
    return answer[:-1]