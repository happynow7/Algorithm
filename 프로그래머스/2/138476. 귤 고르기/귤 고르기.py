from collections import Counter

def solution(k, tangerine):
    type_cnt = Counter(tangerine)
    sorted_counts = sorted(type_cnt.items(), key=lambda x: x[1], reverse=True)
    
    total = 0
    for i, (size, count) in enumerate(sorted_counts, 1):
        total += count
        if total >= k:
            return i
    
    return len(sorted_counts)
