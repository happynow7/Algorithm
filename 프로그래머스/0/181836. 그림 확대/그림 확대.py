def solution(picture, k):
    answer = []
    
    for row in picture:
        expanded_row = ''.join(pixel * k for pixel in row)
        for _ in range(k):
            answer.append(expanded_row)
    
    return answer