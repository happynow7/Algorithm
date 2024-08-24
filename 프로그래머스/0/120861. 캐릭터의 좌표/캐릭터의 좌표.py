def solution(keyinput, board):
    answer = []
    x, y = 0, 0
    xmax = board[0]//2
    ymax = board[1]//2
    
    for i in keyinput:
        if i == 'left' and x > -xmax: x -= 1
        elif i == 'right' and x < xmax: x += 1
        elif i == 'down' and y > -ymax: y -= 1
        elif i == 'up' and y < ymax: y += 1
        
    answer = [x, y]
    return answer