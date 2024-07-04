def solution(answers):
    answer = []
    score = [0,0,0]
    
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)) :
        if answers[i] == pattern1[i%5] :
            score[0] += 1
        if answers[i] == pattern2[i%8] :
            score[1] += 1
        if answers[i] == pattern3[i%10] :
            score[2] += 1
        
    for idx, num in enumerate(score) :
        if num == max(score) :
            answer.append(idx +1)
    
    return answer