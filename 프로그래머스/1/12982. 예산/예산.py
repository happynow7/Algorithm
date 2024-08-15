def solution(d, budget):
    answer = 0
    cnt = 0
    d.sort()
    
    for i in range(len(d)):
        if budget >= d[i]:
            budget -= d[i]
            cnt += 1
        else:
            break
        answer = cnt
    return answer