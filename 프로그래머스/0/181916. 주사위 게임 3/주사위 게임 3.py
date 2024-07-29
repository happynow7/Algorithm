def solution(a, b, c, d):
    dice = [a, b, c, d]
    cnt = [dice.count(item) for item in dice]
    answer = 0
    
    if max(cnt)==4:
        answer = a*1111
    
    elif max(cnt)==3:
        answer = (10 * (dice[cnt.index(3)]) + (dice[cnt.index(1)]))**2       
    
    elif max(cnt)==2:    
        if 1 in cnt:
            answer = dice[cnt.index(1)] * dice[cnt.index(1, cnt.index(1)+1,4)]
            
        else:
            for item in dice:
                if a!=item:
                    answer = (a+item) * abs(a-item)
        
    else:
        answer = min(dice)

    return answer