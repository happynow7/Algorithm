def solution(n):
    answer = 0
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    answer = len(num)
    
    return answer