def solution(participant, completion):
    #딕셔너리 생성
    players = {} 
    
    for p in participant:
        if p in players:
            players[p] += 1
        else:
            players[p] =1
    for c in completion:
        players[c] -= 1
        
    for answer in players:
        if players[answer] > 0:
            return answer