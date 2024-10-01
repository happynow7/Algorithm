def solution(n, left, right):
    result = []
    
    # left부터 right까지 배열의 값 생성
    for i in range(left, right + 1):
        row = i // n  # 해당 인덱스가 속한 행
        col = i % n   # 해당 인덱스가 속한 열
        result.append(max(row, col) + 1)
    
    return result
