from collections import Counter

def solution(k, tangerine):
    tan_type = 0
    tan_cnt = 0
    
    type_cnt = Counter(tangerine)
    type_cnt = sorted(type_cnt.values(), reverse=True)
    
    for cnt in type_cnt:
        tan_cnt += cnt
        tan_type += 1
        if tan_cnt >= k:
            break
    return tan_type