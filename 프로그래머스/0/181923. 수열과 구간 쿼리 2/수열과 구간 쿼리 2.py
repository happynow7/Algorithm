def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        value = []      
        for i in range(s, e+1):
            if arr[i] > k:
                value.append(arr[i])
        if len(value) == 0:
            answer.append(-1)
        else:
            answer.append(min(value))
    return answer