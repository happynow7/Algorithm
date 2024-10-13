def solution(s):
    answer = 0
    min_length = len(s)
    
    if len(s) == 1:
        return 1
    
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1
        
        for j in range(step, len(s), step):
            if prev == s[j:j+step]:
                count += 1
            else:
                compressed += str(count) + prev if count > 1 else prev
                prev = s[j:j+step]
                count = 1
        
        compressed += str(count) + prev if count > 1 else prev
        min_length = min(min_length, len(compressed))
        answer = min_length
    return answer