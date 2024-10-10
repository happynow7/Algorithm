def solution(s):
    answer = True
    icnt = 0
    ycnt = 0
    
    for i in s.lower():
        if(i == 'p'):
            icnt += 1
        elif(i == 'y'):
            ycnt += 1
            
    if(icnt == ycnt):
        answer = True
    else:
        answer = False
        
    return answer