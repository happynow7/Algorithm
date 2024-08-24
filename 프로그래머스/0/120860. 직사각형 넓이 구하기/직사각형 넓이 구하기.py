def solution(dots):
    answer = 0
    xmin = 256
    xmax = -256
    ymin = 256
    ymax = -256
    for i in dots:
        if(i[0] > xmax): xmax = i[0]
        if(i[0] < xmin): xmin = i[0]
        if(i[1] > ymax): ymax = i[1]
        if(i[1] < ymin): ymin = i[1]
    answer = (xmax - xmin) * (ymax - ymin)
    
    return answer