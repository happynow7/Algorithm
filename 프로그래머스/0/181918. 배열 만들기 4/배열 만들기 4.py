def solution(arr):
    stk = []
    i = 0
    
    while i < len(arr):
        if len(stk) > 0:
            if arr[i] > stk[-1]:
                stk.append(arr[i])
                i += 1
            else:
                stk.pop()
        else:
            stk.append(arr[i])
            i += 1
        
    return stk