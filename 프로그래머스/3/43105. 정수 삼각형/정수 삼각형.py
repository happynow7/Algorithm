def solution(triangle):
    answer = 0

    for i in range(1, len(triangle)): # i = 몇번째 줄인지
        for j in range(i+1): # j = 줄 안에서 인덱스
            if j == 0: # 가장 왼쪽인 경우
                triangle[i][j] += triangle[i-1][j]
            elif j == i: # 가장 오른쪽인 경우
                triangle[i][j] += triangle[i-1][-1]
            else: # 가운데인 경우
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
                
        answer = max(triangle[-1])
    return answer