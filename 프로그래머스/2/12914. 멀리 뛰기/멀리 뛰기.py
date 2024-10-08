def solution(n):
    answer = 0
    
    if n < 3:
        return n
    else:
        d = [0] * (n+1)
        d[1], d[2] = 1, 2
        for i in range (3, n+1):
            d[i] = d[i-1] + d[i-2]
    answer = d[n] % 1234567
    return answer