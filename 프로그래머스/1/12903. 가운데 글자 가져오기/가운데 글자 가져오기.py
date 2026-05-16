def solution(s):
    length = len(s)
    center = length//2
    
    if(length%2 == 1):
        return s[center]
    else:
        return s[center-1:center+1]