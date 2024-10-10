def solution(numbers):
    answer = ''
    newnum = list(map(str, numbers))
    
    newnum.sort(key=lambda x: x * 10, reverse=True)
    
    answer = ''.join(newnum)
    
    if(answer[0] == '0'):
        answer  = '0'

    return answer