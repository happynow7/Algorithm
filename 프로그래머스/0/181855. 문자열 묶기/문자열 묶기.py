def solution(strArr):
    answer = 0
    cnt = [0 for _ in range(31)]
    
    for s in strArr:
        cnt[len(s)] += 1
    answer = max(cnt)
    
    return answer
