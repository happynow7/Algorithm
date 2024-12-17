def solution(l, r):
    answer = []
    
    for i in range(l, r+1):
        if all(num in ['0', '5'] for num in str(i)):
            answer.append(i)
            
    if len(answer) == 0:
        answer.append(-1)
    
    return answer


def solution(l, r):
    answer = []
    for i in range(l, r + 1):
        if not set(str(i)) - set(['0', '5']):
            answer.append(i)
    return answer if answer else [-1]