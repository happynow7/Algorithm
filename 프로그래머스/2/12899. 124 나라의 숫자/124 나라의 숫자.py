def solution(n):
    answer = ''
    
    while n:
        t = n % 3
        if not t:
            t = 4
            n -= 1
        answer += str(t)
        n //= 3
    
    return ''.join(answer[::-1])
