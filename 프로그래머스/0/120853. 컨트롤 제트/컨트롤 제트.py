def solution(s):
    answer = 0
    l = s.split(' ')
    stack = []
    
    for i in range(len(l)):
        if l[i] == 'Z':
            if stack:
                stack.pop()
        else:
            stack.append(int(l[i]))
    answer = sum(stack)
    return answer
