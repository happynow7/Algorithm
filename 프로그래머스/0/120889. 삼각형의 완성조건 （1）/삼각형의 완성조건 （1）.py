def solution(sides):
    answer = 0
    m = max(sides)
    sides.sort()
    sides.pop()
    
    if(sides[0] + sides[1] > m):
        answer = 1
    else:
        answer = 2
        
        
def solution(sides):
    sides.sort()
    return 1 if sides[0] + sides[1] > sides[2] else 2        
        