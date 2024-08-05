def solution(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        elif len(stack) != 0 and s[i] == ')' and stack[-1] == '(':
            stack.pop()
        elif len(stack) == 0 and s[i] == ')':
            stack.append(s[i])
    if len(stack) == 0:
        answer = True
    else:
        answer = False
    return answer