from collections import deque

def solution(s):
    answer = 0
    n = len(s)
    check = deque(s)
    
    for i in range(n):
        stack = []
        for j in range(n):
            c = check[j]
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            else:
                if not stack:
                    break
                if c == ")" and stack[-1] == "(":
                    stack.pop()
                elif c == "]" and stack[-1] == "[":
                    stack.pop()
                elif c == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    break
        else:
            if not stack:
                answer += 1
        check.rotate(-1)
    
    return answer
