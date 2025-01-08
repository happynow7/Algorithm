#  SOL1
def solution(topping):
    answer = 0
    for i in range(1,len(topping)):
        a=set(topping[:i])
        b=set(topping[i:])
        if len(a)==len(b):
            answer+=1
    return answer

# SOL2
from collections import Counter
 
def solution(topping):
    answer = 0
    chulsu = Counter(topping) 
    brother = set()
    
    for t in topping:
        chulsu[t] -= 1
        brother.add(t)
        
        if chulsu[t] == 0:
            chulsu.pop(t)
            
        if len(chulsu) == len(brother):
            answer += 1
            
    return answer