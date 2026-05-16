def solution(s, n):
    answer = ''
    
    for al in s:
        
        if al == ' ':
            answer += ' '
            
            
        elif al.islower():
            answer += chr((ord(al) - ord('a') + n) % 26 + ord('a'))

        else:
            answer += chr((ord(al) - ord('A') + n) % 26 + ord('A'))
    
    return answer