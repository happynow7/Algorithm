def solution(arr):
    answer = []
    for i in arr:
        if answer[-1:] == [i]: continue
        answer.append(i)
    return answer
# 
def solution(arr):
    result = []
    for i in range(len(arr)):
        if i == 0 or arr[i - 1] != arr[i]:
            result.append(arr[i])
    return result