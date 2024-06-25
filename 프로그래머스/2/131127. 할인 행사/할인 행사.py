from collections import Counter 

def solution(want, number, discount):
    answer = 0
    
    sign_day = dict(zip(want,number))
    
    for i in range(len(discount)-9):
        if sign_day == Counter(discount[i:i +10]):
            answer +=1
    
    return answer