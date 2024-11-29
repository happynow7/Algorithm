def solution(n):
    answer = ''
    
    for i in range (1, n+1):
        if(i%2 == 0):
            answer += '박'
        elif(i%2 == 1):
            answer += '수'
    
    return answer