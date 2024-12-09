def solution(absolutes, signs):
    answer = 123456789
    sum = 0
    
    for i in range(len(absolutes)):
        if(signs[i] == True):
            sum += absolutes[i] * (+1)
        elif(signs[i] == False):
            sum += absolutes[i] * (-1)
            
    answer = sum
    return answer