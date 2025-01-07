def solution(my_string):
    word = my_string.split(' ')
    answer = int(word[0])
    
    for i in range(len(word)):
        if word[i] == '+':
            answer += int(word[i+1])
        elif word[i] == '-':
            answer -= int(word[i+1])
        else:
            continue
    
    return answer

def solution(my_string):
    return eval(my_string)