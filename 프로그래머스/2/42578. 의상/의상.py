def solution(clothes):
    type_cnt = {}
    answer = 1
    
    for wear, kind in clothes:
        type_cnt[kind] = type_cnt.get(kind, 0) +1
        
    for kind in type_cnt:
        answer *= (type_cnt[kind] + 1 )
    
    return answer -1