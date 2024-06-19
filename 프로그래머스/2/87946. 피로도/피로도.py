from itertools import permutations
def solution(k, dungeons):
    answer = 0
    
    for order in permutations(dungeons,len(dungeons)) :
        hp = k
        cnt = 0
        for i in range(len(dungeons)) :
            if order[i][0] <= hp :
                hp -= order[i][1]
                cnt += 1
        answer = max(answer,cnt)
        
    return answer