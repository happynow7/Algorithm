def solution(before, after):
    answer = 0
    
    if(sorted(before[::-1]) == sorted(after)):
        answer = 1
    else:
        answer = 0
    
    return answer