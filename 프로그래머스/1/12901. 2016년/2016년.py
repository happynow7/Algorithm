def solution(a, b):
    answer = ''
    week = ['THU', 'FRI', 'SAT','SUN', 'MON', 'TUE','WED']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    total = sum(month[:a-1]) + b
    answer = week[total % 7]
    
    return answer