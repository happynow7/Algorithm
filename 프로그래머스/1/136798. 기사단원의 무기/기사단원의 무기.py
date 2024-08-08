def solution(number, limit, power):
    answer = 0
    
    result = [1] * number
    for i in range(1, number + 1):
        li = list()
        for j in range(1, int(i ** 0.5) + 1):
            if (i % j == 0):
                li.append(j)
                li.append(i // j)
        
        if (len(set(li)) > limit):
            result[i - 1] = power
        else:
            result[i - 1] = len(set(li))
            
    answer = sum(result)
    
    return answer