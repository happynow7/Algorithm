def solution(name, yearning, photo):
    answer = []
    info = dict(zip(name, yearning))
    
    for people in photo:
        score = 0
        for i in people:
            score += info.get(i, 0)
        answer.append(score)
    
    return answer