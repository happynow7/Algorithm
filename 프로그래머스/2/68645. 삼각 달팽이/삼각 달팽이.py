def solution(n):
    triangle = [[0] * i for i in range(1, n+1)]
    x, y = -1, 0
    num = 1
    
    for i in range(n):
        for _ in range(i, n):
            if i % 3 == 0:  # Down
                x += 1
            elif i % 3 == 1:  # Right
                y += 1
            else:  # Up-left
                x -= 1
                y -= 1
            
            triangle[x][y] = num
            num += 1
    
    return [num for row in triangle for num in row]