def solution(n):
    answer = 0
    na = []
    
    for i in range(1, n+1):
        if(n%i==1):
            na.append(i)
            
    answer = na[0]
    return answer