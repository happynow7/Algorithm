def solution(board):
    n = len(board)
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    
    # 위험 지역 표시
    for x in range(n):
        for y in range(n):
            if board[x][y] == 1:
                for i in range(8):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 1:
                        board[nx][ny] = 2  # 2는 위험 지역을 나타냄
    
    # 안전 지역 계산
    return sum(row.count(0) for row in board)
