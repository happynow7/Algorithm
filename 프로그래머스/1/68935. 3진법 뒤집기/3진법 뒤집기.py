def solution(n):
    answer = 0
    arr = []

    while n > 0:
        arr += str(n % 3)
        n //= 3

    arr = arr[::-1]
    cnt = 1

    for i in arr:
        answer += int(i) * cnt
        cnt *= 3
        
    return answer