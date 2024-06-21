from collections import Counter

def solution(participant, completion):
    answer = ''
    
    participant_counter = Counter(participant)
    completion_counter = Counter(completion)
    incomplete = participant_counter - completion_counter
    answer = list(incomplete.elements())[0]
    
    return answer